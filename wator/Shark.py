import random

from wator.Fish import Fish


class Shark(Fish):
    """A fish with teeth"""

    def __init__(self, agent_id, environment, pos_x=0, pos_y=0, color=(253, 108, 158, 255), breed_time=10,
                 starve_time=3):
        super().__init__(agent_id, environment, pos_x, pos_y, color, breed_time)
        self.starveTime = starve_time
        self.energyLeft = starve_time
    
    def update(self, sma):
        self.age += 1
        if self.age == 5:
            self.color = (255, 0, 0, 255)
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
        old_x, old_y = self.posX, self.posY
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        destinations = []
        while directions:
            d = random.choice(directions)
            (self.stepX, self.stepY) = d
            next_pos_x, next_pos_y = self.posX + self.stepX, self.posY + self.stepY
            if self.environment.torus:
                next_pos_x = next_pos_x % self.environment.width
                next_pos_y = next_pos_y % self.environment.height
            try:
                target = self.environment.get(next_pos_x, next_pos_y)
                if target is None:
                    destinations.append(d)
                elif type(target) == Fish:
                    self.eat(sma)
                    self.environment.move(self)
                    if self.breedTick >= self.breedTime:
                        child = self.clone()
                        child.agentId = sma.nextAgentId
                        sma.nextAgentId += 1
                        child.posX, child.posY = old_x, old_y
                        child.color = (253, 108, 158, 255)
                        self.environment.place(child, old_x, old_y)
                        sma.birthList.append(child)
                        self.breedTick = 0
                    return
            except IndexError as _:
                pass
            directions.remove(d)
        self.move(destinations, sma)

    def move(self, destinations, sma):
        if not destinations:
            return
        old_x, old_y = self.posX, self.posY

        (self.stepX, self.stepY) = random.choice(destinations)

        self.environment.move(self)
        if self.breedTick >= self.breedTime:
            child = self.clone()
            child.agentId = sma.nextAgentId
            sma.nextAgentId += 1
            child.posX, child.posY = old_x, old_y
            child.color = (253, 108, 158, 255)
            self.environment.place(child, old_x, old_y)
            sma.birthList.append(child)
            self.breedTick = 0

    def clone(self):
        return Shark(self.agentId, self.environment, self.posX, self.posY, (253, 108, 158, 255), self.breedTime,
                     self.starveTime)
