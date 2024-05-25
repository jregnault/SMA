import logging

from core.Agent import Agent
from core.Environment import Environment
from core.Error import BounceError


class Particle(Agent):
    """A simple ball that bounce against walls and other balls"""

    def __init__(self, agent_id: int, environment: Environment, pos_x: int = 0, pos_y: int = 0, step_x: int = 0,
                 step_y: int = 0, color: [int, int, int, int] = (150, 150, 150, 255)) -> None:
        """Creates a particle
        Parameters:
            agent_id: The particle's unique id
            environment: The environment to put the particle in
            pos_x: The initial X position of the particle in the environment
            pos_y: The initial Y position of the particle in the environment
            pos_x: The initial X translation of the particle in the environment
            pos_y: The initial Y translation of the particle in the environment
            color: The color of the particle
        """
        super().__init__(agent_id, environment, pos_x, pos_y, step_x, step_y, color)

    def will_hit_a_wall(self):
        """Return True if the next move is illegal in terms of boundaries,
        False otherwise"""
        if self.environment.torus:
            return False
        else:
            next_pos_x = self.posX + self.stepX
            next_pos_y = self.posY + self.stepY

            try:
                self.environment.get(next_pos_x, next_pos_y)
                return False
            except IndexError as _:
                return True
    
    def decide(self, sma):
        """Ask the agent to analyze its environment and take action (or not)"""
        logging.debug(
            f"Agent {self.agentId}: posX = {self.posX}; posY = {self.posY}; stepX = {self.stepX}, stepY = {self.stepY}"
        )
        if self.will_hit_a_wall():
            self.bounce(sma)
        try:
            self.environment.move(self)
        except BounceError as _:
            if self.environment.torus:
                self.bounce(
                    sma,
                    self.environment.get(
                        (self.posX + self.stepX) % self.environment.width,
                        (self.posY + self.stepY) % self.environment.height
                    )
                )
            else:
                if self.will_hit_a_wall():
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
        - target : the agent to bounce against. If set to None, we consider that the agent is bouncing against a wall.
        """
        if target is not None:
            self.color = (250, 0, 0, 255)
            target.color = (250, 0, 0, 255)
            self.posX, target.posX = target.posX, self.posX
            self.posY, target.posY = target.posY, self.posY
        else:
            if self.stepX == 0 or self.stepY == 0:
                # horizontal/vertical movement
                self.stepX *= -1
                self.stepY *= -1
            else:
                # corners
                if (self.posX, self.posY) == (0, 0):
                    self.stepX, self.stepY = 1, 1
                elif (self.posX, self.posY) == (0, self.environment.height - 1):
                    self.stepX, self.stepY = 1, -1
                elif (self.posX, self.posY) == (self.environment.width - 1, 0):
                    self.stepX, self.stepY = -1, 1
                elif (self.posX, self.posY) == (self.environment.width - 1, self.environment.height - 1):
                    self.stepX, self.stepY = -1, -1
                else:
                    # borders
                    if self.posX == 0 or self.posX == self.environment.width - 1:
                        self.stepX *= -1
                    else:
                        self.stepY *= -1

        if sma.trace:
            print("Agent;" + str(self.agentId) + ";" + str(self.posX) + ";" + str(self.posY))
