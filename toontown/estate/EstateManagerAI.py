import functools

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.fsm.FSM import FSM

from toontown.estate import HouseGlobals
from toontown.estate.DistributedHouseAI import DistributedHouseAI
from toontown.toon import ToonDNA


class LoadHouseOperation(FSM):
    def __init__(self, mgr, estate, index, avatar, callback):
        FSM.__init__(self, 'LoadHouseOperation')
        self.mgr = mgr
        self.estate = estate
        self.index = index
        self.avatar = avatar
        self.callback = callback
        self.done = False
        self.houseId = None
        self.house = None
        self.gender = None

    def start(self):
        # We have a few different cases here:
        if self.avatar is None:
            # Case #1: There isn't an avatar in that estate slot. Make a blank house.
            # Because this state completes so fast, we'll use taskMgr to delay
            # it until the next iteration. This solves reentrancy problems.
            taskMgr.doMethodLater(0.0, self.demand, 'makeBlankHouse-%s' % id(self), extraArgs=['MakeBlankHouse'])
            return

        style = ToonDNA.ToonDNA()
        style.makeFromNetString(self.avatar.get('setDNAString')[0])
        self.houseId = self.avatar.get('setHouseId', [0])[0]
        self.gender = style.gender
        if self.houseId == 0:
            # Case #2: There is an avatar, but no setHouseId. Make a new house:
            self.demand('CreateHouse')
        else:
            # Case #3: Avatar with a setHouseId. Load it:
            self.demand('LoadHouse')

    def enterMakeBlankHouse(self):
        self.house = DistributedHouseAI(self.mgr.air)
        self.house.setHousePos(self.index)
        self.house.setColor(self.index)
        self.house.generateWithRequired(self.estate.zoneId)
        self.estate.houses[self.index] = self.house
        self.demand('Off')

    def enterCreateHouse(self):
        self.mgr.air.dbInterface.createObject(self.mgr.air.dbId, self.mgr.air.dclassesByName['DistributedHouseAI'],
                                              {'setName': [self.avatar['setName'][0]],
                                               'setAvatarId': [self.avatar['avId']]}, self.__handleHouseCreated)

    def __handleHouseCreated(self, houseId):
        if self.state != 'CreateHouse':
            # This operation was likely aborted.
            return

        # Update the avatar's houseId:
        av = self.mgr.air.doId2do.get(self.avatar['avId'])
        if av:
            av.b_setHouseId(houseId)
        else:
            self.mgr.air.dbInterface.updateObject(self.mgr.air.dbId, self.avatar['avId'],
                                                  self.mgr.air.dclassesByName['DistributedToonAI'],
                                                  {'setHouseId': [houseId]})

        self.houseId = houseId
        self.demand('LoadHouse')

    def enterLoadHouse(self):
        # Activate the house:
        self.mgr.air.sendActivate(self.houseId, self.mgr.air.districtId, self.estate.zoneId,
                                  self.mgr.air.dclassesByName['DistributedHouseAI'],
                                  {'setHousePos': [self.index],
                                   'setColor': [self.index],
                                   'setName': [self.avatar['setName'][0]],
                                   'setAvatarId': [self.avatar['avId']]})

        # Wait for the house to generate:
        self.acceptOnce('generate-%d' % self.houseId, self.__handleHouseGenerated)

    def __handleHouseGenerated(self, house):
        # The house will need to be able to reference
        # the estate for setting up gardens, so:
        house.estate = self.estate

        # Initialize our interior:
        house.interior.gender = self.gender
        house.interior.start()

        self.house = house
        self.estate.houses[self.index] = self.house
        if config.GetBool('want-gardening', False):
            # Initialize our garden:
            self.house.createGardenManager()

        self.demand('Off')

    def exitLoadHouse(self):
        self.ignore('generate-%d' % self.houseId)

    def enterOff(self):
        self.done = True
        self.callback(self.house)


class LoadEstateOperation(FSM):
    def __init__(self, mgr, callback):
        FSM.__init__(self, 'LoadEstateOperation')
        self.mgr = mgr
        self.callback = callback
        self.estate = None
        self.accId = None
        self.zoneId = None
        self.avIds = None
        self.avatars = None
        self.houseOperations = None
        self.petOperations = None

    def start(self, accId, zoneId):
        self.accId = accId
        self.zoneId = zoneId
        self.demand('QueryAccount')

    def enterQueryAccount(self):
        self.mgr.air.dbInterface.queryObject(self.mgr.air.dbId, self.accId, self.__handleQueryAccount)

    def __handleQueryAccount(self, dclass, fields):
        if self.state != 'QueryAccount':
            # This operation was likely aborted.
            return

        if dclass != self.mgr.air.dclassesByName['AccountAI']:
            self.mgr.notify.warning('Account %d has non-account dclass %d!' % (self.accId, dclass))
            self.demand('Failure')
            return

        self.accFields = fields
        self.estateId = fields.get('ESTATE_ID', 0)
        self.demand('QueryAvatars')

    def enterQueryAvatars(self):
        self.avIds = self.accFields.get('ACCOUNT_AV_SET', [0] * 6)
        self.avatars = {}
        for index, avId in enumerate(self.avIds):
            if avId == 0:
                self.avatars[index] = None
                continue

            self.mgr.air.dbInterface.queryObject(self.mgr.air.dbId, avId,
                                                 functools.partial(self.__handleQueryAvatar, index=index))

    def __handleQueryAvatar(self, dclass, fields, index):
        if self.state != 'QueryAvatars':
            # This operation was likely aborted.
            return

        if dclass != self.mgr.air.dclassesByName['DistributedToonAI']:
            self.mgr.notify.warning(
                'Account %d has avatar %d with non-Toon dclass %d!' % (self.accId, self.avIds[index], dclass))
            self.demand('Failure')
            return

        fields['avId'] = self.avIds[index]
        self.avatars[index] = fields
        if len(self.avatars) == 6:
            self.__gotAllAvatars()

    def __gotAllAvatars(self):
        # We have all of our avatars, so now we can handle the estate.
        if self.estateId:
            # We already have an estate, so let's load that:
            self.demand('LoadEstate')
        else:
            # We don't yet have an estate, so let's make one:
            self.demand('CreateEstate')

    def enterCreateEstate(self):
        # Create a blank estate object:
        self.mgr.air.dbInterface.createObject(self.mgr.air.dbId, self.mgr.air.dclassesByName['DistributedEstateAI'], {},
                                              self.__handleEstateCreated)

    def __handleEstateCreated(self, estateId):
        if self.state != 'CreateEstate':
            # This operation was likely aborted.
            return

        self.estateId = estateId

        # Store the new estate object on our account:
        self.mgr.air.dbInterface.updateObject(self.mgr.air.dbId, self.accId, self.mgr.air.dclassesByName['AccountAI'],
                                              {'ESTATE_ID': estateId})

        self.demand('LoadEstate')

    def enterLoadEstate(self):
        # Set the estate fields:
        fields = {'setSlot%dToonId' % i: (avId,) for i, avId in enumerate(self.avIds)}

        # Activate the estate:
        self.mgr.air.sendActivate(self.estateId, self.mgr.air.districtId, self.zoneId,
                                  self.mgr.air.dclassesByName['DistributedEstateAI'], fields)

        # Wait for the estate to generate:
        self.acceptOnce('generate-%d' % self.estateId, self.__handleEstateGenerated)

    def __handleEstateGenerated(self, estate):
        # Get the estate:
        self.estate = estate

        # For keeping track of pets in this estate:
        self.estate.pets = []

        # Map the owner to the estate:
        ownerId = self.mgr.getOwnerFromZone(self.estate.zoneId)
        owner = self.mgr.air.doId2do.get(ownerId)
        if owner:
            self.mgr.toon2estate[owner] = self.estate

        # Set the estate's ID list:
        self.estate.b_setIdList(self.avIds)

        # Load houses:
        self.demand('LoadHouses')

    def exitLoadEstate(self):
        self.ignore('generate-%d' % self.estateId)

    def enterLoadHouses(self):
        self.houseOperations = []
        for houseIndex in xrange(6):
            houseOperation = LoadHouseOperation(self.mgr, self.estate, houseIndex, self.avatars[houseIndex],
                                                self.__handleHouseLoaded)
            self.houseOperations.append(houseOperation)
            houseOperation.start()

    def __handleHouseLoaded(self, house):
        if self.state != 'LoadHouses':
            # We aren't loading houses, so we probably got cancelled. Therefore,
            # the only sensible thing to do is simply destroy the house.
            house.requestDelete()
            return

        # A house operation just finished! Let's see if all of them are done:
        if all(houseOperation.done for houseOperation in self.houseOperations):
            # Load our pets:
            self.demand('LoadPets')

    def enterLoadPets(self):
        self.petOperations = []
        for houseIndex in xrange(6):
            av = self.avatars[houseIndex]
            if av and av['setPetId'][0] != 0:
                petOperation = LoadPetOperation(self.mgr, self.estate, av, self.__handlePetLoaded)
                self.petOperations.append(petOperation)
                petOperation.start()

        if not self.petOperations:
            taskMgr.doMethodLater(0, lambda: self.demand('Finished'), 'no-pets', extraArgs=[])

    def __handlePetLoaded(self, pet):
        if self.state != 'LoadPets':
            pet.requestDelete()
            return

        # A pet operation just finished! Let's see if all of them are done:
        if all(petOperation.done for petOperation in self.petOperations):
            self.demand('Finished')

    def enterFinished(self):
        self.petOperations = []
        self.callback(True)

    def enterFailure(self):
        self.cancel()
        self.callback(False)

    def cancel(self):
        if self.estate:
            self.estate.destroy()
            self.estate = None

        self.demand('Off')


class LoadPetOperation(FSM):
    def __init__(self, mgr, estate, toon, callback):
        FSM.__init__(self, 'LoadPetFSM')
        self.mgr = mgr
        self.estate = estate
        self.toon = toon
        self.callback = callback
        self.done = False
        self.petId = 0

    def start(self):
        if type(self.toon) == dict:
            self.petId = self.toon['setPetId'][0]
        else:
            self.petId = self.toon.getPetId()

        if self.petId not in self.mgr.air.doId2do:
            self.mgr.air.sendActivate(self.petId, self.mgr.air.districtId, self.estate.zoneId)
            self.acceptOnce('generate-%d' % self.petId, self.__generated)
        else:
            self.__generated(self.mgr.air.doId2do[self.petId])

    def __generated(self, pet):
        self.pet = pet
        self.estate.pets.append(pet)
        self.demand('Off')

    def enterOff(self):
        self.ignore('generate-%d' % self.petId)
        self.done = True
        self.callback(self.pet)


class EstateManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.toon2estate = {}
        self.estate = {}
        self.estate2toons = {}
        self.estate2timeout = {}
        self.zone2toons = {}
        self.zone2owner = {}
        self.petOperations = []

    def getEstateZone(self, avId, name):
        # Thank you name, very cool!
        senderId = self.air.getAvatarIdFromSender()
        accId = self.air.getAccountIdFromSender()
        senderAv = self.air.doId2do.get(senderId)
        if not senderAv:
            self.air.writeServerEvent('suspicious', senderId, 'Sent getEstateZone() but not on district!')
            return

        # If an avId has been provided, then the sender wants to visit a friend.
        # In this case, we do not need to load the estate, we only need to check
        # to see if it already exists.
        if avId and avId != senderId:
            av = self.air.doId2do.get(avId)
            if av and av.dclass == self.air.dclassesByName['DistributedToonAI']:
                estate = self.toon2estate.get(av)
                if estate:
                    # Found an estate!
                    avId = estate.owner.doId
                    zoneId = estate.zoneId
                    self._mapToEstate(senderAv, estate)

                    # In case the sender is teleporting from their estate
                    # to another estate, we want to unload their estate.
                    self._unloadEstate(senderAv)

                    if senderAv and senderAv.getPetId() != 0:
                        pet = self.air.doId2do.get(senderAv.getPetId())
                        if pet:
                            self.acceptOnce(self.air.getAvatarExitEvent(senderAv.getPetId()), self.__handleLoadPet,
                                            extraArgs=[estate, senderAv])
                            pet.requestDelete()
                        else:
                            self.__handleLoadPet(estate, senderAv)

                    # Now we want to send the sender to the estate.
                    if hasattr(senderAv, 'enterEstate'):
                        senderAv.enterEstate(avId, zoneId)

                    self.sendUpdateToAvatarId(senderId, 'setEstateZone', [avId, zoneId])

            # We weren't able to find the given avId at an estate, that's pretty sad.
            self.sendUpdateToAvatarId(senderId, 'setEstateZone', [0, 0])
            return

        # Otherwise, the sender wants to go to their own estate.
        estate = getattr(senderAv, 'estate', None)
        if estate:
            # The sender already has an estate loaded, so let's send them there.
            self._mapToEstate(senderAv, senderAv.estate)

            if senderAv and senderAv.getPetId() != 0:
                pet = self.air.doId2do.get(senderAv.getPetId())
                if pet:
                    self.acceptOnce(self.air.getAvatarExitEvent(senderAv.getPetId()), self.__handleLoadPet,
                                    extraArgs=[estate, senderAv])
                    pet.requestDelete()
                else:
                    self.__handleLoadPet(estate, senderAv)

            if hasattr(senderAv, 'enterEstate'):
                senderAv.enterEstate(senderId, estate.zoneId)

            self.sendUpdateToAvatarId(senderId, 'setEstateZone', [senderId, estate.zoneId])

            # If a timeout is active, cancel it:
            if estate in self.estate2timeout:
                self.estate2timeout[estate].remove()
                del self.estate2timeout[estate]

            return

        if getattr(senderAv, 'loadEstateOperation', None):
            # We already have a loading operation underway; ignore this second
            # request since the first operation will setEstateZone() when it
            # finishes anyway.
            return

        zoneId = self.air.allocateZone()
        self.zone2owner[zoneId] = avId

        def estateLoaded(success):
            if success:
                senderAv.estate = senderAv.loadEstateOperation.estate
                senderAv.estate.owner = senderAv
                self._mapToEstate(senderAv, senderAv.estate)
                if hasattr(senderAv, 'enterEstate'):
                    senderAv.enterEstate(senderId, zoneId)

                self.sendUpdateToAvatarId(senderId, 'setEstateZone', [senderId, zoneId])
            else:
                # Estate loading failed. Sad!
                self.sendUpdateToAvatarId(senderId, 'setEstateZone', [0, 0])

                # Might as well free up the zoneId as well.
                self.air.deallocateZone(zoneId)
                del self.zone2owner[zoneId]

            senderAv.loadEstateOperation = None

        self.acceptOnce(self.air.getAvatarExitEvent(senderAv.doId), self.__handleUnexpectedExit, extraArgs=[senderAv])

        if senderAv and senderAv.getPetId() != 0:
            pet = self.air.doId2do.get(senderAv.getPetId())
            if pet:
                self.acceptOnce(self.air.getAvatarExitEvent(senderAv.getPetId()), self.__handleLoadEstate,
                                extraArgs=[senderAv, estateLoaded, accId, zoneId])
                pet.requestDelete()
                return

        self.__handleLoadEstate(senderAv, estateLoaded, accId, zoneId)

    def __handleUnexpectedExit(self, senderAv):
        self._unmapFromEstate(senderAv)
        self._unloadEstate(senderAv)

    def exitEstate(self):
        senderId = self.air.getAvatarIdFromSender()
        senderAv = self.air.doId2do.get(senderId)
        if not senderAv:
            self.air.writeServerEvent('suspicious', senderId, 'Sent exitEstate() but not on district!')
            return

        self._unmapFromEstate(senderAv)
        self._unloadEstate(senderAv)

    def removeFriend(self, ownerId, avId):
        if not (ownerId or avId):
            return

        owner = self.air.doId2do.get(ownerId)
        if not owner:
            return

        friend = self.air.doId2do.get(avId)
        if not friend:
            return

        estate = self.estate.get(ownerId)
        if not estate:
            return

        if ownerId not in estate.getIdList():
            return

        toons = self.estate2toons.get(estate, [])
        if owner not in toons and friend not in toons:
            return

        friendInList = False
        for friendPair in owner.getFriendsList():
            if type(friendPair) == tuple:
                friendId = friendPair[0]
            else:
                friendId = friendPair

            if friendId == avId:
                friendInList = True
                break

        if not friendInList:
            self.sendUpdateToAvatarId(friend.doId, 'sendAvToPlayground', [friend.doId, 1])

    def _unloadEstate(self, av):
        if getattr(av, 'estate', None):
            estate = av.estate
            if estate not in self.estate2timeout:
                self.estate2timeout[estate] = taskMgr.doMethodLater(HouseGlobals.BOOT_GRACE_PERIOD, self._cleanupEstate,
                                                                    estate.uniqueName('unload-estate'),
                                                                    extraArgs=[estate])

            # Send warning:
            self._sendToonsToPlayground(av.estate, 0)

        if getattr(av, 'loadEstateOperation', None):
            self.air.deallocateZone(av.loadEstateOperation.zoneId)
            av.loadEstateOperation.cancel()
            av.loadEstateOperation = None

        if av and hasattr(av, 'exitEstate') and hasattr(av, 'isInEstate') and av.isInEstate():
            av.exitEstate()

        if av and av.getPetId() != 0:
            self.ignore(self.air.getAvatarExitEvent(av.getPetId()))
            pet = self.air.doId2do.get(av.getPetId())
            if pet:
                pet.requestDelete()

        self.ignore(self.air.getAvatarExitEvent(av.doId))

    def _mapToEstate(self, av, estate):
        self._unmapFromEstate(av)
        self.estate[av.doId] = estate
        self.estate2toons.setdefault(estate, []).append(av)
        if av not in self.toon2estate:
            self.toon2estate[av] = estate

        self.zone2toons.setdefault(estate.zoneId, []).append(av.doId)

    def _unmapFromEstate(self, av):
        estate = self.toon2estate.get(av)
        if not estate:
            return

        try:
            del self.estate[av.doId]
        except KeyError:
            pass

        del self.toon2estate[av]
        try:
            self.estate2toons[estate].remove(av)
        except (KeyError, ValueError):
            pass

        try:
            self.zone2toons[estate.zoneId].remove(av.doId)
        except (KeyError, ValueError):
            pass

    def _cleanupEstate(self, estate):
        # Boot all avatars from estate:
        self._sendToonsToPlayground(estate, 1)

        # Clean up avatar <-> estate mappings:
        for av in self.estate2toons.get(estate, []):
            try:
                del self.estate[av.doId]
                del self.toon2estate[av]
            except KeyError:
                pass

        try:
            del self.estate2toons[estate]
        except KeyError:
            pass

        try:
            del self.zone2toons[estate.zoneId]
        except KeyError:
            pass

        # Clean up timeout, if it exists:
        if estate in self.estate2timeout:
            del self.estate2timeout[estate]

        # Destroy estate and unmap from owner:
        estate.destroy()
        estate.owner.estate = None

        # Destroy pets:
        for pet in estate.pets:
            pet.requestDelete()

        estate.pets = []

        # Free estate's zone:
        self.air.deallocateZone(estate.zoneId)
        del self.zone2owner[estate.zoneId]

    def _sendToonsToPlayground(self, estate, reason):
        for toon in self.estate2toons.get(estate, []):
            self.sendUpdateToAvatarId(toon.doId, 'sendAvToPlayground', [toon.doId, reason])

    def getEstateZones(self, ownerId):
        toon = self.air.doId2do.get(ownerId)
        if not toon:
            return []

        estate = self.toon2estate.get(toon)
        if not estate:
            return []

        return [estate.zoneId]

    def getEstateHouseZones(self, ownerId):
        houseZones = []
        toon = self.air.doId2do.get(ownerId)
        if not toon:
            return houseZones

        estate = self.toon2estate.get(toon)
        if not estate:
            return houseZones

        houses = estate.houses
        for house in houses:
            houseZones.append(house.interiorZone)

        return houseZones

    def getOwnerFromZone(self, zoneId):
        return self.zone2owner.get(zoneId, 0)

    def __handleLoadPet(self, estate, av):
        petOperation = LoadPetOperation(self, estate, av, self.__handlePetLoaded)
        self.petOperations.append(petOperation)
        petOperation.start()

    def __handlePetLoaded(self, _):
        # A pet operation just finished! Let's see if all of them are done:
        if all(petOperation.done for petOperation in self.petOperations):
            self.petOperations = []

    def __handleLoadEstate(self, av, callback, accId, zoneId):
        self._unmapFromEstate(av)
        av.loadEstateOperation = LoadEstateOperation(self, callback)
        av.loadEstateOperation.start(accId, zoneId)
