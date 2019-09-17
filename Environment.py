import numpy as np

import Agent

class Environment:

    def __init__(self, width=100, height=100, isToric=False):
        self.space = np.empty((width, height), dtype=Agent.Agent , order='F')
        self.isToric = isToric
        self.agents = []
    
    def addAgent(self, agent, x, y):
        if self.space[y][x] == None:
            self.space[y][x] = agent
            self.agents.append(agent)
        else:
            raise ValueError("The position is already taken")