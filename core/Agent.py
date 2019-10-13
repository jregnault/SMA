import pygame

class Agent:
    """Abstract agent"""

    def __init__(self, agentID, environment, posX = 0, posY = 0, direction = (1,1), color = (150,150,150,255)):
        self.agentID = agentID
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.color = color
    
    def decide(self, sma):
        pass

    def draw(self, view):
        """Draw the agent on the surface.
        Parameters:
        -----------
        - view : the view associated to the SMA.
        """
        boxSize = view.boxSize
        x = self.posX * boxSize + (boxSize / 2)
        y = self.posY * boxSize + (boxSize / 2)
        if self.environment.torus:
            x += self.posX + 1
            y += self.posY + 1

        pygame.draw.circle(view.screen, self.color, [x,y], boxSize / 2)