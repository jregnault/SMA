from core.Agent import Agent


class Particle(Agent):
    """A simple ball that bounce against walls and other balls"""

    def __init__(self, environment, posX = 0, posY = 0, direction = (1,1), color = (150,150,150,255)):
        super().__init__(environment,posX,posY,direction,color)
