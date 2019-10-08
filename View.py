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
        for i in range(0,self.environment.width+1):
            pos = i * self.boxSize + i
            pygame.draw.line(
                gridView,
                (0,0,0,0),
                (pos,0),
                (pos,height-1))
    
        for j in range(0,self.environment.height+1):
            pos = j * self.boxSize + j
            pygame.draw.line(
                gridView,
                (0,0,0,0),
                (0,pos),
                (width-1,pos)
            )

        return gridView

    def drawAgent(self, agent):
        agentView = pygame.Surface((self.boxSize,self.boxSize))
        agentView = agentView.convert_alpha()
        agentView.fill((0,0,0,0))

        pygame.draw.circle(
            agentView,
            agent.color,
            (int(agentView.get_width()/2), int(agentView.get_height()/2)),
            int(self.boxSize/2),
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
                (agent.posX * self.boxSize + agent.posX + 1,
                 agent.posY * self.boxSize + agent.posY + 1)
            )

        self.screen.blit(background,(0,0))
        pygame.display.flip()