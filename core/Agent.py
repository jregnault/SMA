import pygame


class Agent:
    """Abstract agent"""

    def __init__(self, agent_id, environment, pos_x=0, pos_y=0, step_x=0, step_y=0, color=(150, 150, 150, 255)):
        self.agentId = agent_id
        self.environment = environment
        self.posX = pos_x
        self.posY = pos_y
        self.stepX = step_x
        self.stepY = step_y
        self.color = color
        self.isAlive = True
    
    def die(self, sma):
        """make the agent die"""
        self.isAlive = False
        self.color = (0, 0, 0, 255)
        self.environment.remove(self.posX, self.posY)
        if sma.trace:
            print("Agent;" + str(self.agentId) + ";" + str(self.posX) + ";" + str(self.posY) + ";" + "0")
    
    def decide(self, sma):
        pass

    def draw(self, view):
        """Draw the agent on the surface.
        Parameters:
        -----------
        - view : the view associated to the SMA.
        """
        box_size = view.boxSize
        x = self.posX * box_size + box_size / 2
        y = self.posY * box_size + box_size / 2
        if view.grid:
            x += self.posX + 1
            y += self.posY + 1

        pygame.draw.circle(view.screen, self.color, (int(x), int(y)), int(box_size / 2), 0)
