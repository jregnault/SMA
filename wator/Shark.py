import random

from wator.Fish import Fish
from core.Error import BounceError

class Shark(Fish):
    """A fish with teeth"""

    def __init__(self, agentId, environment, posX = 0, posY = 0, color = (253,108,158,255), breedTime = 10, starveTime = 3):
        super().__init__(agentId, environment, posX, posY, color, breedTime)
        self.starveTime = starveTime
        self.energyLeft = starveTime
    
    