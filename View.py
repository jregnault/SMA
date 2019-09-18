import pygame
from pygame.locals import *

import Agent

class View:
    def __init__(self, canvasSizeX, canvasSizeY, boxSize, grid):
        self.canvasSizeX = canvasSizeX
        self.canvasSizeY = canvasSizeY
        pygame.init()
        self.screen = pygame.display.set_mode((canvasSizeX,canvasSizeY))
        pygame.display.set_caption("S.M.A.")
    
    def drawBackground(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250,250,250))

    def drawGrid(self):
        self.grid = pygame.Surface(self.screen.get_size())
        self.grid = self.grid.convert()
        self.grid.fill((250,250,250,255))

        width = self.grid.get_width()
        height = self.grid.get_height()
        for i in range(0,width, width/self.canvasSizeX):
            pygame.draw.line(self.grid, (0,0,0), (i,0), (i,height-1))
    
        for j in range(0,height, height/self.canvasSizeY):
            pygame.draw.line(self.grid, (0,0,0), (0,j), (width-1,j))

        self.background.blit(self.grid, (0,0))

    def drawAgent(self, agent):
        agent = pygame.Surface((self.background.get_width()/self.canvasSizeX,self.background.get_height()/self.canvasSizeY))
        agent = agent.convert_alpha()
        agent.set_alpha(255)

        if agent.isBouncing:
            pygame.draw.circle(agent,(250,0,0,0),(agent.get_width()/2,agent.get_height()/2),agent.get_width()/2,width=0)
        else:
            pygame.draw.circle(agent,(0,0,0,0),(agent.get_width()/2,agent.get_height()/2),agent.get_width()/2,width=0)
        
        self.background.blit(agent, (agent.posX * (self.background.get_width()/self.canvasSizeX), agent.posY * (self.background.get_height() / self.canvasSizeY)))

    def update(self, observable):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()