import random

class Agent:

    def __init__(self, environment, posX = 0, posY = 0, stepX = random.randint(-1,1), stepY = random.randint(-1,1), color = "grey"):
        self.posX = posX
        self.posY = posY
        self.stepX = stepX
        self.stepY = stepY
        self.color = color
        self.environment = environment
    
    def update(self):
        pass

    def decide(self):
        pass

    def move(self):
        self.posX += self.stepX
        self.posY += self.stepY
    
    def bounce(self):
        pass