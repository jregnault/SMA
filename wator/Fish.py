import random

from core.Agent import Agent
from core.Error import BounceError

class Fish(Agent):
    """A fish agent that can die and reproduce"""

    def __init__(self, agentId, environment, posX = 0, posY = 0, color = (255,255,0,255), breedTime = 2):
        super().__init__(agentId, environment, posX, posY, 0, 0, color)
        self.age = 0
        self.breedTime = breedTime
        self.breedTick = random.randint(0,breedTime)
    
    def update(self, sma):
        self.age += 1
        if self.age == 5:
            self.color = (0,255,0,255)
        self.breedTick += 1

    def decide(self, sma):
        oldX, oldY = self.posX, self.posY
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while directions != []:
            (self.stepX, self.stepY) = random.choice(directions)
            directions.remove((self.stepX,self.stepY))
            try:
                self.environment.move(self)
                if self.breedTick >= self.breedTime:
                    child = self.clone()
                    child.agentId = sma.nextAgentId
                    sma.nextAgentId += 1
                    child.posX, child.posY = oldX, oldY
                    child.color = (255,255,0,255)
                    if sma.trace:
                        print("Agent;" + str(child.agentId) + ";" + str(child.posX) + ";" + str(child.posY) + ";" + "1")
                    sma.birthList.append(child)
                    self.environment.place(child, oldX, oldY)
                    self.breedTick = 0
                return
            except BounceError as _:
                pass
    
    def clone(self):
        return Fish(self.agentId, self.environment, self.posX, self.posY, (255,255,0,255), self.breedTime)