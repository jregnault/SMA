import random

import Environment

class Agent:

    def __init__(self, environment, posX = 0, posY = 0, stepX = random.randint(-1,1), stepY = random.randint(-1,1), color = (150,150,150,0)):
        self.posX = posX
        self.posY = posY
        self.stepX = stepX
        self.stepY = stepY
        self.color = color
        self.environment = environment

    def willHitAWall(self):
        return (self.posX == 0 and self.stepX < 0) or (self.posX == self.environment.width-1 and self.stepX > 0) or (self.posY == 0 and self.stepY < 0) or (self.posY == self.environment.height-1 and self.stepY > 0)
            

    def decide(self):
        pass

    def move(self):
        self.color = (150,150,150,0)
        self.environment.move(self)
        self.posX += self.stepX
        self.posY += self.stepY

    def bounce(self, target=None):
        self.color = (250,0,0,0)
        if target == None:
            if self.posX == 0 or self.posX == self.environment.getWidth() - 1:
                self.stepX *= -1
            if self.posY == 0 or self.posY == self.environment.getHeight() - 1:
                self.stepY *= -1
        else:
            self.stepX, target.stepX = target.stepX, self.stepX
            self.stepY, target.stepY = target.stepY, self.stepY