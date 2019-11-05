from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.suit.Suit import *
from direct.task.Task import Task
import math

class BossHealthBar:
    def __init__(self):
        self.bossBar = DirectWaitBar(pos=(0.0, 0, 0.94), relief=DGG.SUNKEN, frameSize=(-2.0, 2.0, -0.2, 0.2), borderWidth=(0.02, 0.02), scale=0.23, range=100, sortOrder=50, frameColor=(0.5, 0.5, 0.5, 0.5), barColor=(0.75, 0.75, 1.0, 0.7), text='0/0', text_scale=0.35, text_fg=(1, 1, 1, 1), text_align=TextNode.ACenter, text_pos=(0, -0.1))
        self.bossBar.hide()
        self.healthCondition = 0
        self.bossBarColors = Suit.healthColors
        for color in self.bossBarColors:
            color -= (0, 0, 0, 0.2)

    def initialize(self, hp, maxhp):
        self.bossBar['text'] = ('%s / %s' % (str(hp), str(maxhp)))
        newhp = hp / maxhp
        self.bossBar['range'] = maxhp
        self.bossBar['value'] = hp
        self.bossBar['barColor'] = self.bossBarColors[self.healthCondition]
        self.bossBar.show()

    def update(self, hp, maxhp):
        newhp = hp
        if newhp < 0:
            newhp = 0
        self.bossBar['text'] = ('%s / %s' % (str(newhp), str(maxhp)))
        if hp > 0:
            newhp = hp
            self.bossBar['value'] = newhp
        else:
            self.bossBar['value'] = 0
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
                taskMgr.add(blinkTask, 'blink-task')
            elif condition == 5:
                if self.healthCondition == 4:
                    taskMgr.remove('blink-task')
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, 'blink-task')
            else:
                self.bossBar['barColor'] = (self.bossBarColors[condition])
            self.healthCondition = condition

    def __blinkRed(self, task):
            self.bossBar['barColor'] = self.bossBarColors[3]
            return Task.done

    def __blinkGray(self, task):
            self.bossBar['barColor'] = self.bossBarColors[4]
            return Task.done

    def cleanUp(self):
        if self.bossBar:
            self.bossBar.destroy()
            self.bossBar = None
            taskMgr.remove('blink-task')
            self.healthCondition = 0
