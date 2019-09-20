import numpy as np
import random

import Agent

class Environment:

    def __init__(self, gridSizeX=100, gridSizeY=100, torus=False):
        self.space = np.empty((gridSizeX, gridSizeY), dtype=Agent.Agent , order='F')
        self.torus = torus
        self.agents = []
    
    def addAgent(self, agent, x, y):
        if self.space[y][x] == None:
            self.space[y][x] = agent
            self.agents.append(agent)
        else:
            self.addAgent(agent,random.randint(0,self.getWidth()-1),random.randint(0,self.getHeight()-1))

    
    def getAgent(self, x, y):
        pass
    
    def isEmpty(self, x, y):
        pass

    def getHeight(self):
        return len(self.space[0])
    
    def getWidth(self):
        return len(self.space)