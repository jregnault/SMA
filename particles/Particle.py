import logging

from core.Agent import Agent
from core.Error import BounceError

class Particle(Agent):
    """A simple ball that bounce against walls and other balls"""

    def __init__(self, environment, pos_x = 0, pos_y = 0, step_x = 0, step_y = 0, color = (150, 150, 150, 255)):
        super().__init__(environment, pos_x, pos_y, step_x, step_y, color)

    def willHitAWall(self):
        """Return True if the next move is illegal in terms of boundaries,
        False otherwise"""
        if self.environment.torus:
            return False
        else:
            nextPosX = self.posX + self.stepX
            nextPosY = self.posY + self.stepY

            try:
                self.environment.get(nextPosX,nextPosY)
                return False
            except IndexError as _:
                return True
    
    def decide(self, sma):
        """Ask the agent to analyze its environment and take action (or not)"""
        logging.debug("Agent %d: posX = %d; posY = %d; stepX = %d, stepY = %d", self.agentId, self.posX, self.posY, self.stepX, self.stepY)
        if self.willHitAWall():
            self.bounce(sma)
        try:
            self.environment.move(self)
        except BounceError as _:
            if self.environment.torus:
                self.bounce(sma, self.environment.get((self.posX + self.stepX) % self.environment.width, (self.posY + self.stepY) % self.environment.height))
            else:
                if self.willHitAWall():
                    self.bounce(sma)
                else:
                    self.bounce(sma, self.environment.get(self.posX + self.stepX, self.posY + self.stepY))
            try:
                self.environment.move(self)
            except BounceError as _:
                pass

    def bounce(self, sma, target=None):
        """Change the direction according to the situation.
        Parameters:
        -----------
        - target : the agent to bounce against. If setted to None, we consider that the agent is bouncing against a wall.
        """
        if target != None:
            self.color = (250,0,0,255)
            target.color = (250,0,0,255)
            self.posX, target.posX = target.posX, self.posX
            self.posY, target.posY = target.posY, self.posY
        else:
            if self.stepX == 0 or self.stepY == 0:
                # horizontal/vertical movement
                self.stepX *= -1
                self.stepY *= -1
            else:
                # corners
                if (self.posX, self.posY) == (0,0):
                    self.stepX, self.stepY = 1, 1
                elif (self.posX, self.posY) == (0,self.environment.height - 1):
                    self.stepX, self.stepY = 1, -1
                elif (self.posX, self.posY) == (self.environment.width - 1, 0):
                    self.stepX, self.stepY = -1, 1
                elif (self.posX, self.posY) == (self.environment.width -1, self.environment.height -1):
                    self.stepX, self.stepY = -1, -1
                else:
                    # borders
                    if self.posX == 0 or self.posX == self.environment.width - 1:
                        self.stepX *= -1
                    else:
                        self.stepY *= -1

        if sma.trace:
            print("Agent;" + str(self.agentId) + ";" + str(self.posX) + ";" + str(self.posY))