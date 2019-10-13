
class Agent:
    """Abstract agent"""
    def __init__(self, idAgent, environment, posX = 0, posY = 0, direction = (0,0), color = (150,150,150,255)):
        self.id = idAgent
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.color = color
        self.environment = environment
    
    def decide(self):
        pass

	def move(self):
		pass