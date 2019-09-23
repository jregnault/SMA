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
        self.isBouncing = False
    
    def update(self):
        pass

    def decide(self):
        neighbors = self.environment.getNeighborhood(self,2)
        if neighbors == []:
            
        if 0 <= (self.posX + self.stepX) < self.environment.getWidth() and 0 <= (self.posY + self.stepY) < self.environment.getHeight():
            if self.environment.isEmpty(self.posX + self.stepX, self.posY + self.stepY):
                self.isBouncing = False
                self.move()
            else:
                self.agentBounce(self.environment.getAgent(self.posX + self.stepX, self.posY + self.stepY))
        else:
            self.wallBounce()

    def move(self):
        self.posX += self.stepX
        self.posY += self.stepY

    def wallBounce(self):
        self.isBouncing = True
        self.color = (250,0,0,0)
        if self.posX == 0 or self.posX == self.environment.getWidth() - 1:
            self.stepX *= -1
        if self.posY == 0 or self.posY == self.environment.getHeight() -1:
            self.stepY *= -1
    
    def agentBounce(self, agent):
        self.isBouncing = True
        self.color = (250,0,0,0)
        self.stepX, agent.stepX = agent.stepX, self.stepX
        self.stepY, agent.stepY = agent.stepY, self.stepY
