import numpy as np
import random

import Agent

class Environment:

    def __init__(self, gridSizeX=100, gridSizeY=100, torus=False):
        self.width = gridSizeX
        self.height = gridSizeY
        self.space = np.empty((gridSizeX, gridSizeY), dtype=Agent.Agent , order='F')
        self.torus = torus
    
    def add(self, agent, x, y):
        if self.space[x][y] == None:
            self.space[x][y] = agent
        else:
            raise ValueError("Add : the cell is already taken !")
    
    def remove(self, x, y):
        self.space[x][y] = None

    def move(self,agent):
        if self.torus:
            if agent.stepX >= 0:
                if agent.stepY >= 0:
                    self.add(agent, agent.posX + agent.stepX % self.width, agent.posY + agent.stepY % self.height)
                else:
                    self.add(agent, agent.posX + agent.stepX % self.width, agent.posY + agent.stepY % self.height)
        else:
            self.add(agent, agent.posX + agent.stepX, agent.posY + agent.stepY)
        self.remove(agent.posX, agent.posY)

    def get(self, x, y):
        return self.space[x][y]
    
    def isEmpty(self, x, y):
        return self.space[x][y] == None