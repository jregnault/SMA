import pygame


class Agent:
    """Abstract agent"""

    def __init__(self, agent_id, environment, color=(150, 150, 150, 255)):
        self.agentId = agent_id
        self.environment = environment
        self.color = color
        self.isAlive = True
    
    def die(self, sma):
        """make the agent die"""
        self.isAlive = False
        self.color = (0,0,0,255)
        self.environment.remove(self.posX, self.posY)
        if sma.trace:
            print("Agent;" + str(self.agentId) + ";" + str(self.posX) + ";" + str(self.posY) + ";" + "0")
    
    def decide(self, environment):
        pass

    def draw(self, view):
        """Draw the agent on the surface.
        Parameters:
        -----------
        - view : the view associated to the SMA.
        """
        boxSize = view.boxSize
        x = self.posX * boxSize + boxSize / 2
        y = self.posY * boxSize + boxSize / 2
        if view.grid:
            x += self.posX + 1
            y += self.posY + 1

        pygame.draw.circle(view.screen, self.color, (int(x),int(y)), int(boxSize / 2),0)