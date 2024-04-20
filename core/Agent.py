import pygame

import core


class Agent:
    """Abstract agent"""

    def __init__(self, agent_id: int, environment: core.Environment, pos_x: int = 0, pos_y: int = 0, step_x: int = 0,
                 step_y: int = 0, color: tuple[int, int, int, int] = (150, 150, 150, 255)):
        """Creates a new agent
        Parameters:
            agent_id : The unique identifier for the agent.
            environment : The environment in which the agent is.
            pos_x : The agent's position on the X axis of the environment. Default to 0.
            pos_y : The agent's position on the Y axis of the environment. Default to 0.
            step_x : The distance on the X axis the agent moves every turn. Default to 0.
            step_y : The distance on the Y axis the agent moves every turn. Default to 0.
            color : The agent's color.
        """
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
