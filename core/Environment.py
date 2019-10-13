import numpy as np

from core.Agent import Agent

class Environment:

    def __init__(self, view, gridSizeX=100, gridSizeY=100, torus=False, color=(0,0,0)):
        self.width = gridSizeX
        self.height = gridSizeY
        self.space = np.empty((gridSizeX, gridSizeY), dtype=Agent.Agent , order='F')
        self.torus = torus
        self.color = color
        self.view = view