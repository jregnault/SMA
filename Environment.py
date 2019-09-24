import numpy as np
import random

import Agent

class Environment:

    def __init__(self, gridSizeX=100, gridSizeY=100, torus=False):
        self.width = gridSizeX
        self.height = gridSizeY
        self.space = np.empty((gridSizeX, gridSizeY), dtype=Agent.Agent , order='F')
        self.torus = torus
        self.agents = []
    
    def addAgent(self, agent, x, y):
        if self.space[y][x] == None:
            self.space[y][x] = agent
            self.agents.append(agent)
        else:
            self.addAgent(agent,random.randint(0,self.width()-1),random.randint(0,self.height()-1))
    
    def getAgent(self, x, y):
        return self.space[x][y]
    
    def getNeighborhood(self, agent, distance):
        neighbors = []
        if self.torus:
            wmin = (agent.posX - distance) % self.width()
            wmax = (agent.posX + distance) % self.width()
            hmin = (agent.posY - distance) % self.height()
            hmax = (agent.posY + distance) % self.height()
        else:
            wmin = max(0,agent.posX - distance)
            wmax = min(self.width()-1,agent.posX + distance)
            hmin = max(0,agent.posY - distance)
            hmax = min(self.height()-1,agent.posY + distance)
        
        for y in range(hmin,hmax+1):
            for x in range(wmin,wmax+1):
                a = self.getAgent(x,y)
                if a != None:
                    neighbors.append(a)
        
        return neighbors

    def isEmpty(self, x, y):
        return self.space[x][y] == None