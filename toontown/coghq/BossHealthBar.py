from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.suit.Suit import *
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *

class BossHealthBar:

    def __init__(self):
        self.bossBarStartPosZ = 1.5
        self.bossBarEndPosZ = 0.88
        self.bossBarFrameBg = loader.loadTexture('phase_9/maps/HealthBarBosses.png')
        self.bossBarFrame = DirectFrame(pos=(0, 0, self.bossBarStartPosZ), scale=1.8, sortOrder=20)
        self.gui = loader.loadModel('phase_9/models/gui/HealthBarBosses')
        self.gui.setTexture(self.bossBarFrameBg)
        self.gui.setTransparency(1)
        self.bossBar = DirectWaitBar(relief=DGG.SUNKEN, scale=(0.197, 0, 0.135), value=100, pos=(-0.005, 0, 0.002), frameSize=(-2.0, 2.0, -0.2, 0.2), borderWidth=(0.02, 0.02), range=100, sortOrder=50, frameColor=(0.5, 0.5, 0.5, 0.6), barColor=(0.75, 0.75, 1.0, 0.7), text='0 / 0', text_scale=(0.3, 0.4), text_fg=(1, 1, 1, 1), text_align=TextNode.ACenter, text_pos=(0, -0.12), text_shadow=(0, 0, 0, 1))
        self.gui.hide()
        self.bossBar.hide()
        self.gui.reparentTo(self.bossBarFrame)
        self.bossBar.reparentTo(self.bossBarFrame)
        self.healthCondition = 0
        self.currHp = 0
        self.newHp = 0
        self.maxHp = 0
        self.healthRatio = 0
        self.isUpdating = False
        self.isBlinking = False
        self.bossBarColors = (Vec4(0, 1, 0, 0.8),
                              Vec4(1, 1, 0, 0.8),
                              Vec4(1, 0.5, 0, 0.8),
                              Vec4(1, 0, 0, 0.8),
                              Vec4(0.3, 0.3, 0.3, 0.8))
        self.colorThresholds = (0.65, 0.4, 0.2, 0.1, 0.05)

    def initialize(self, hp, maxhp):
        self.maxHp = maxhp
        self.newHp = hp
        self.currHp = hp
        self.bossBar['text'] = ('%s / %s' % (str(hp), str(maxhp)))
        self.bossBar['range'] = maxhp
        self.bossBar['value'] = hp
        self.__checkUpdateColor(hp, maxhp)
        self.bossBar.show()
        self.gui.show()
        seq = Sequence(self.bossBarFrame.posInterval(1.0, Point3(0, 0, self.bossBarEndPosZ), blendType='easeOut'))
        seq.start()

    def update(self, hp, maxHp):
        if self.isUpdating:
            taskMgr.remove('bar-smooth-update-task')
            self.isUpdating = False
        self.newHp = hp
        if self.newHp < 0:
            self.newHp = 0
        if self.maxHp != 0:
            if self.currHp != self.newHp:
                smoothUpdateTask = Task.loop(Task(self.__smoothUpdate), Task.pause(0.01))
                taskMgr.add(smoothUpdateTask, 'bar-smooth-update-task')
                self.isUpdating = True

    def __checkUpdateColor(self, hp, maxhp):
        if self.bossBar:
            self.healthRatio = float(hp) / float(maxhp)
            if self.healthRatio > self.colorThresholds[0]:
                condition = 0
            elif self.healthRatio > self.colorThresholds[1]:
                condition = 1
            elif self.healthRatio > self.colorThresholds[2]:
                condition = 2
            elif self.healthRatio > self.colorThresholds[3]:
                condition = 3
            elif self.healthRatio > self.colorThresholds[4]:
                condition = 4
            else:
                condition = 5
            self.__applyNewColor(condition)
            if self.healthCondition != condition:
                if condition == 4:
                    if self.healthCondition == 5:
                        taskMgr.remove('bar-blink-task')
                        self.isBlinking = False
                    blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75), Task(self.__blinkGray), Task.pause(0.1))
                    taskMgr.add(blinkTask, 'bar-blink-task')
                    self.isBlinking = True
                elif condition == 5:
                    if self.healthCondition == 4:
                        taskMgr.remove('bar-blink-task')
                        self.isBlinking = False
                    blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
                    taskMgr.add(blinkTask, 'bar-blink-task')
                    self.isBlinking = True
                else:
                    if self.isBlinking:
                        taskMgr.remove('bar-blink-task')
                        self.isBlinking = False
                self.healthCondition = condition

    def __applyNewColor(self, currColor):
        if self.bossBar:
            if currColor != 3 and currColor != 4 and currColor != 5:
                if self.healthRatio > self.colorThresholds[0]:
                    condition = 0
                elif self.healthRatio > self.colorThresholds[1]:
                    condition = 1
                elif self.healthRatio > self.colorThresholds[2]:
                    condition = 2
                if condition > 0:
                    numeratorRatioAmt = self.colorThresholds[condition - 1]
                else:
                    numeratorRatioAmt = 1
                denominatorRatioAmt = self.colorThresholds[condition]
                numeratorColorAmt = self.bossBarColors[condition]
                denominatorColorAmt = self.bossBarColors[condition + 1]
                currentRatioAmt = numeratorRatioAmt - self.healthRatio
                totalRatioAmt = numeratorRatioAmt - denominatorRatioAmt
                ratioRatio = currentRatioAmt / totalRatioAmt
                differenceColorAmt = denominatorColorAmt - numeratorColorAmt
                ratioColorToAdd = differenceColorAmt * ratioRatio
                totalColorAmt = self.bossBarColors[condition] + ratioColorToAdd
                self.bossBar['barColor'] = totalColorAmt

    def __blinkRed(self, task):
        if self.bossBar:
            self.bossBar['barColor'] = self.bossBarColors[3]
            return Task.done
        else:
            taskMgr.remove('bar-blink-task')

    def __blinkGray(self, task):
        if self.bossBar:
            self.bossBar['barColor'] = self.bossBarColors[4]
            return Task.done
        else:
            taskMgr.remove('bar-blink-task')

    def __smoothUpdate(self, task):
        if self.bossBar:
            if self.currHp != self.newHp:
                posOrNeg = self.currHp - self.newHp
                if posOrNeg > 0:
                    if posOrNeg == 1:
                        self.currHp -= 1
                    else:
                        self.currHp -= 2
                elif posOrNeg < 0:
                    if posOrNeg == -1:
                        self.currHp += 1
                    else:
                        self.currHp += 2
                self.bossBar['text'] = ('%s / %s' % (str(self.currHp), str(self.maxHp)))
                self.bossBar['value'] = self.currHp
                self.__checkUpdateColor(self.currHp, self.maxHp)
            elif self.currHp == self.newHp:
                self.isUpdating = False
                taskMgr.remove('bar-smooth-update-task')
            return Task.done

    def deinitialize(self):
        seq = Sequence(self.bossBarFrame.posInterval(1.0, Point3(0, 0, self.bossBarStartPosZ), blendType='easeIn'))
        seq.start()

    def cleanup(self):
        if self.bossBarFrame:
            self.bossBarFrame.destroy()
            del self.bossBarFrame
            if self.bossBar:
                if self.isUpdating:
                    taskMgr.remove('bar-smooth-update-task')
                self.bossBar.destroy()
                del self.bossBar
                if self.isBlinking:
                    taskMgr.remove('bar-blink-task')
                self.healthCondition = 0
