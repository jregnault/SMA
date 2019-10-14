import random

from core.Agent import Agent

class Fish(Agent):
    """A fish agent that can die and reproduce"""

    def __init__(self, agentId, environment, posX = 0, posY = 0, color = (255,255,0,255), breedTime = 2):
        super().__init__(agentId, environment, posX, posY, 0, 0, color)
        self.breedTime = breedTime
    