import numpy as np

from core.Agent import Agent
from core.Error import TileNotEmptyError, BounceError

class Environment:

    def __init__(self, gridSizeX=100, gridSizeY=100, torus=False, color=(0,0,0)):
        self.width = gridSizeX
        self.height = gridSizeY
        self.space = np.empty((gridSizeX, gridSizeY), dtype=Agent , order='F')
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
        if self.space[x][y] == None:
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
        nextPosX = agent.posX + agent.direction[0]
        nextPosY = agent.posY + agent.direction[1]

        if self.torus:
            nextPosX = nextPosX % self.width
            nextPosY = nextPosY % self.height
        else:
            if nextPosX < 0 or nextPosX >= self.width or nextPosY < 0 or nextPosY >= self.height:
                raise BounceError()
        
        if self.space[nextPosX][nextPosY] == None:
            self.space[nextPosX][nextPosY] = agent
            agent.posX = nextPosX
            agent.posY = nextPosY
        else:
            raise BounceError()

    def get(self, x, y):
        """Returns the content of the tile (x,y)."""
        return self.space[x][y]