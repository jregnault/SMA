import numpy as np

from core.Agent import Agent
from core.Error import TileNotEmptyError

class Environment:

    def __init__(self, view, gridSizeX=100, gridSizeY=100, torus=False, color=(0,0,0)):
        self.width = gridSizeX
        self.height = gridSizeY
        self.space = np.empty((gridSizeX, gridSizeY), dtype=Agent , order='F')
        self.torus = torus
        self.color = color
        self.view = view
    
    def place(self, agent, x, y):
        """Try to place an agent at a specified position.
        Raise TileNotEmptyError if the tile is already occupied by another agent.
        Parameters:
        -----------
        - agent : the agent to place in the environment
        - x : the x position
        - y : the y position
        """
        if self.space[x][y] == None:
            self.space[x][y] = agent
        else:
            raise TileNotEmptyError()
    
    def remove(self, x, y):
        """Sets the given position to None."""
        self.space[x][y] = None