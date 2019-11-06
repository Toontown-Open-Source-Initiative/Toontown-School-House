from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.suit.Suit import *
from direct.task.Task import Task

class BossHealthBar:
    def __init__(self):
        self.bossBar = DirectWaitBar(pos=(0.0, 0, 0.94), relief=DGG.SUNKEN, frameSize=(-2.0, 2.0, -0.2, 0.2), borderWidth=(0.02, 0.02), scale=0.23, range=100, sortOrder=50, frameColor=(0.5, 0.5, 0.5, 0.5), barColor=(0.75, 0.75, 1.0, 0.7), text='0/0', text_scale=0.35, text_fg=(1, 1, 1, 1), text_align=TextNode.ACenter, text_pos=(0, -0.1), text_shadow=(0, 0, 0, 1))
        self.bossBar.hide()
        self.healthCondition = 0
        self.currHp = 0
        self.newHp = 0
        self.maxHp = 0
        self.isUpdating = False
        self.isBlinking = False
        self.bossBarColors = Suit.healthColors
        for color in self.bossBarColors:
            color -= (0, 0, 0, 0.2)

    def initialize(self, hp, maxhp):
        self.maxHp = maxhp
        self.newHp = hp
        self.currHp = hp
        self.bossBar['text'] = ('%s / %s' % (str(hp), str(maxhp)))
        self.bossBar['range'] = maxhp
        self.bossBar['value'] = hp
        self.bossBar['barColor'] = self.bossBarColors[self.healthCondition]
        self.bossBar.show()

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
        health = float(hp) / float(maxhp)
        if health > 0.95:
            condition = 0
        elif health > 0.7:
            condition = 1
        elif health > 0.3:
            condition = 2
        elif health > 0.05:
            condition = 3
        elif health > 0.0:
            condition = 4
        else:
            condition = 5
        if self.healthCondition != condition:
            if condition == 4:
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
                self.bossBar['barColor'] = (self.bossBarColors[condition])
            self.healthCondition = condition


    def __blinkRed(self, task):
        self.bossBar['barColor'] = self.bossBarColors[3]
        return Task.done

    def __blinkGray(self, task):
        self.bossBar['barColor'] = self.bossBarColors[4]
        return Task.done

    def __smoothUpdate(self, task):
        if self.bossBar:
            if self.currHp != self.newHp:
                posOrNeg = self.currHp - self.newHp
                if posOrNeg > 0:
                    self.currHp -= 1
                elif posOrNeg < 0:
                    self.currHp += 1
                self.bossBar['text'] = ('%s / %s' % (str(self.currHp), str(self.maxHp)))
                self.bossBar['value'] = self.currHp
                self.__checkUpdateColor(self.currHp, self.maxHp)
            elif self.currHp == self.newHp:
                self.isUpdating = False
                taskMgr.remove('bar-smooth-update-task')
            return Task.done

    def cleanUp(self):
        if self.bossBar:
            if self.isUpdating:
                taskMgr.remove('bar-smooth-update-task')
            self.bossBar.destroy()
            self.bossBar = None
            if self.isBlinking:
                taskMgr.remove('bar-blink-task')
            self.healthCondition = 0
