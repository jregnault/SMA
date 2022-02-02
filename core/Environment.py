import numpy as np

from core.Agent import Agent
from core.Error import TileNotEmptyError, BounceError


class Environment:

    def __init__(self, grid_size_x=100, grid_size_y=100, torus=False, color=(255, 255, 255)):
        self.width = grid_size_x
        self.height = grid_size_y
        self.space = np.empty((grid_size_x, grid_size_y), dtype=Agent, order='F')
        self.torus = torus
        self.color = color
    
    def place(self, agent, x, y):
        """Try to place an agent at a specified position.
        Raise TileNotEmptyError if the tile is already occupied by another agent.
        Parameters:
        -----------
        - agent : the agent to place in the environment
        - x : the x position
        - y : the y position
        """
        if self.space[x][y] is None:
            self.space[x][y] = agent
        else:
            raise TileNotEmptyError()
    
    def remove(self, x, y):
        """Sets the given position to None."""
        self.space[x][y] = None
    
    def move(self, agent):
        """Move an agent based on its direction. Raise BounceError if the movement is illegal.
        Parameters:
        -----------
        - agent : the agent that tries to move
        """
        next_pos_x = agent.posX + agent.stepX
        next_pos_y = agent.posY + agent.stepY

        if self.torus:
            next_pos_x = next_pos_x % self.width
            next_pos_y = next_pos_y % self.height
        else:
            if next_pos_x < 0 or next_pos_x >= self.width or next_pos_y < 0 or next_pos_y >= self.height:
                raise BounceError()
        
        if self.space[next_pos_x][next_pos_y] is None:
            self.space[next_pos_x][next_pos_y] = agent
            self.remove(agent.posX, agent.posY)
            agent.posX = next_pos_x
            agent.posY = next_pos_y
        else:
            raise BounceError()

    def get(self, x, y):
        """Returns the content of the tile (x,y)."""
        return self.space[x][y]
