from core.Agent import Agent


class Particle(Agent):
    """A simple ball that bounce against walls and other balls"""

    def __init__(self, environment, posX = 0, posY = 0, direction = (1,1), color = (150,150,150,255)):
        super().__init__(environment,posX,posY,direction,color)

    def willHitAWall(self):
        if self.environment.torus:
            return False
        else:
            nextPosX = self.posX + self.direction[0]
            nextPosY = self.posY + self.direction[1]

            try:
                self.environment.get(nextPosX,nextPosY)
                return False
            except IndexError as _:
                return True
    
    def decide(self):
        if self.willHitAWall():
            self.bounce()
            self.decide()
        try:
            self.move()
        except BounceError as _:
            if self.environment.torus:
                self.bounce(self.environment.get(self.posX + self.direction[0] % self.environment.width, self.posY + self.direction[1] % self.environment.height))
            else:
                self.bounce(self.environment.get(self.posX + self.direction[0], self.posY + self.direction[1]))
            try:
                self.move()
            except BounceError as _:
                pass
    