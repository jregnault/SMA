from core.Agent import Agent


class Particle(Agent):
    """A simple ball that bounce against walls and other balls"""

    def __init__(self, environment, posX = 0, posY = 0, direction = (1,1), color = (150,150,150,255)):
        super().__init__(environment,posX,posY,direction,color)

    def willHitAWall(self):
        """Return True if the next move is illegal in terms of boundaries,
        False otherwise"""
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
        """Ask the agent to analyze its environment and take action (or not)"""
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
    
    def move(self):
        """Ask the environment to move the agent."""
        self.environment.move(self)

    def bounce(self, target=None):
        """Change the direction according to the situation.
        Parameters:
        -----------
        - target : the agent to bounce against. If setted to None, we consider that the agent is bouncing against a wall.
        """
        if target != None:
            self.posX, target.posX = target.posX, self.posX
            self.posY, target.posY = target.posY, self.posY
        else:
            if self.posX == 0 or self.posX == self.environment.width - 1:
                self.direction[0] *= -1
            if self.posY == 0 or self.posY == self.environment.height - 1:
                self.direction[1] *= -1