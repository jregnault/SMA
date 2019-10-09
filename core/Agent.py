
NEXT_AGENT_ID = 1

class Agent:
    """Abstract agent"""
    def __init__(self, environment, posX = 0, posY = 0, direction = (0,0), color = (150,150,150,255)):
        self.id = NEXT_AGENT_ID
        NEXT_AGENT_ID += 1
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.color = color
        self.environment = environment
    
    def decide(self):
        pass