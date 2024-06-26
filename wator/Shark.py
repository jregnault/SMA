import random

from wator.Fish import Fish
from core.Error import BounceError

class Shark(Fish):
    """A fish with teeth"""

    def __init__(self, agentId, environment, posX = 0, posY = 0, color = (253,108,158,255), breedTime = 10, starveTime = 3):
        super().__init__(agentId, environment, posX, posY, color, breedTime)
        self.starveTime = starveTime
        self.energyLeft = starveTime
    
    def update(self, sma):
        self.age += 1
        if self.age == 5:
            self.color = (255,0,0,255)
        self.breedTick += 1
        self.energyLeft -= 1
        if self.energyLeft == 0:
            self.die(sma)
    
    def eat(self, sma):
        x, y = self.posX + self.stepX, self.posY + self.stepY
        if self.environment.torus:
            x = x % self.environment.width
            y = y % self.environment.height
        target = self.environment.get(x, y)
        target.die(sma)
        self.energyLeft = self.starveTime
        if sma.trace:
            print("Shark;" + str(self.agentId) + ";" + str(self.posX) + ";" + str(self.posY))

    def decide(self, sma):
        oldX, oldY = self.posX, self.posY
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        dests = []
        while directions != []:
            d = random.choice(directions)
            (self.stepX, self.stepY) = d
            nextPosX, nextPosY = self.posX + self.stepX, self.posY + self.stepY
            if self.environment.torus:
                nextPosX = nextPosX % self.environment.width
                nextPosY = nextPosY % self.environment.height
            try:
                target = self.environment.get(nextPosX, nextPosY)
                if target == None:
                    dests.append(d)
                elif type(target) == Fish:
                    self.eat(sma)
                    self.environment.move(self)
                    if self.breedTick >= self.breedTime:
                        child = self.clone()
                        child.agentId = sma.nextAgentId
                        sma.nextAgentId += 1
                        child.posX, child.posY = oldX, oldY
                        child.color = (253,108,158,255)
                        self.environment.place(child, oldX, oldY)
                        sma.birthList.append(child)
                        self.breedTick = 0
                    return
            except IndexError as _:
                pass
            directions.remove(d)
        self.move(dests, sma)

    def move(self, dests, sma):
        if dests == []:
            return
        oldX, oldY = self.posX, self.posY

        (self.stepX, self.stepY) = random.choice(dests)

        self.environment.move(self)
        if self.breedTick >= self.breedTime:
            child = self.clone()
            child.agentId = sma.nextAgentId
            sma.nextAgentId += 1
            child.posX, child.posY = oldX, oldY
            child.color = (253,108,158,255)
            self.environment.place(child, oldX, oldY)
            sma.birthList.append(child)
            self.breedTick = 0

    def clone(self):
        return Shark(self.agentId, self.environment, self.posX, self.posY, (253,108,158,255), self.breedTime, self.starveTime)