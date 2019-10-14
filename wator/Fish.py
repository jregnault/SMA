import random

from core.Agent import Agent
from core.Error import BounceError

class Fish(Agent):
    """A fish agent that can die and reproduce"""

    def __init__(self, agentId, environment, posX = 0, posY = 0, color = (255,255,0,255), breedTime = 2):
        super().__init__(agentId, environment, posX, posY, 0, 0, color)
        self.breedTime = breedTime
        self.breedTick = 0
    
    def decide(self, sma):
        oldX, oldY = self.posX, self.posY
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while directions != []:
            (self.stepX, self.stepY) = random.choice(directions)
            directions.remove((self.stepX,self.stepY))
            try:
                self.environment.move(self)
                if self.breedTick == self.breedTime:
                    child = self.clone()
                    child.posX, child.posY = oldX, oldY
                    sma.birthList.append(child)
                    self.environment.place(child, oldX, oldY)
                    self.breedTick = 0
                return
            except BounceError as _:
                pass
    
    