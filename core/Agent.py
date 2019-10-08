

class Agent:
    """Abstract agent"""

    def __init__(self, environment, posX = 0, posY = 0, stepX = 0, stepY = 0, color = (150,150,150,255)):
        self.posX = posX
        self.posY = posY
        self.stepX = stepX
        self.stepY = stepY
        self.color = color
        self.environment = environment
    
    def decide(self):
        pass