import random

from core.Agent import Agent
from core.Error import BounceError


class Fish(Agent):
    """A fish agent that can die and reproduce"""

    def __init__(self, agent_id, environment, pos_x=0, pos_y=0, color=(255, 255, 0, 255), breed_time=2):
        super().__init__(agent_id, environment, pos_x, pos_y, 0, 0, color)
        self.age = 0
        self.breedTime = breed_time
        self.breedTick = random.randint(0, breed_time)
    
    def update(self, sma):
        self.age += 1
        if self.age == 5:
            self.color = (0, 255, 0, 255)
        self.breedTick += 1

    def decide(self, sma):
        old_x, old_y = self.posX, self.posY
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while directions:
            (self.stepX, self.stepY) = random.choice(directions)
            directions.remove((self.stepX, self.stepY))
            try:
                self.environment.move(self)
                if self.breedTick >= self.breedTime:
                    child = self.clone()
                    child.agentId = sma.nextAgentId
                    sma.nextAgentId += 1
                    child.posX, child.posY = old_x, old_y
                    child.color = (255, 255, 0, 255)
                    if sma.trace:
                        print("Agent;" + str(child.agentId) + ";" + str(child.posX) + ";" + str(child.posY) + ";" + "1")
                    sma.birthList.append(child)
                    self.environment.place(child, old_x, old_y)
                    self.breedTick = 0
                return
            except BounceError as _:
                pass
    
    def clone(self):
        return Fish(self.agentId, self.environment, self.posX, self.posY, (255, 255, 0, 255), self.breedTime)
