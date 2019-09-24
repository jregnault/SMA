import pygame
from pygame.locals import *

import Agent

class View:
    def __init__(self, environment, canvasSizeX, canvasSizeY, boxSize, grid):
        self.canvasSizeX = canvasSizeX
        self.canvasSizeY = canvasSizeY
        self.boxSize = boxSize
        self.grid = grid
        self.environment = environment
        pygame.init()
        self.screen = pygame.display.set_mode((canvasSizeX,canvasSizeY))
        pygame.display.set_caption("S.M.A.")
    
    def drawBackground(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((250,250,250))
        return background

    def drawGrid(self):
        gridView = pygame.Surface(self.screen.get_size())
        gridView = gridView.convert()
        gridView.fill((250,250,250,255))

        width = gridView.get_width()
        height = gridView.get_height()
        for i in range(0,width, int(width/self.environment.width)):
            pygame.draw.line(
                gridView,
                (0,0,0,0),
                (i,0),
                (i,height-1))
    
        for j in range(0,height, int(height/self.environment.height)):
            pygame.draw.line(gridView, (0,0,0), (0,j), (width-1,j))

        return gridView

    def drawAgent(self, agent):
        agentView = pygame.Surface(self.boxSize)
        agentView = agentView.convert_alpha()
        agentView.fill((0,0,0,0))

        particleSize = min(self.boxSize[0], self.boxSize[1])

        pygame.draw.circle(
            agentView,
            agent.color,
            (int(agentView.get_width()/2), int(agentView.get_height()/2)),
            int(particleSize/2),
            0)
        
        return agentView

    def update(self, observable):
        background = self.drawBackground()
        if self.grid:
            gridView = self.drawGrid()
            background.blit(gridView,(0,0))
        for agent in observable.agentList:
            agentView = self.drawAgent(agent)
            background.blit(
                agentView,
                (agent.posX * self.boxSize[0], agent.posY * self.boxSize[1])
            )

        self.screen.blit(background,(0,0))
        pygame.display.flip()