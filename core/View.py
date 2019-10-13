import pygame
from pygame.locals import *

class View:
    
    def __init__(self, environment, boxSize=1, grid=False):
        self.environment = environment
        self.boxSize = boxSize
        self.grid = grid

        canvasSizeX = environment.width * boxSize
        canvasSizeY = environment.height * boxSize
        if grid:
            canvasSizeX += environment.width + 1
            canvasSizeY += environment.height + 1

        pygame.init()
        self.screen = pygame.display.set_mode((canvasSizeX,canvasSizeY))
        pygame.display.set_caption("Multi-Agent System")
        self.drawBackground()
        if grid:
            self.drawGrid()
    
    def drawBackground(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(self.environment.color)
        self.screen.blit(background,(0,0))

    def drawGrid(self):
        """Add a grid to the view."""
        gridSurface = pygame.Surface(self.screen.get_size())
        gridSurface = gridSurface.convert()
        gridSurface.fill(self.environment.color)

        width = gridSurface.get_width()
        height = gridSurface.get_height()
        for i in range(0, self.environment.width+1):
            pos = i * self.boxSize + i
            pygame.draw.line(gridSurface, (0,0,0,255), (pos,0), (pos,height-1))
        
        for j in range(0, self.environment.height+1):
            pos = j * self.boxSize + j
            pygame.draw.line(gridSurface, (0,0,0,255), (0,pos), (width-1,pos))
        
        self.screen.blit(gridSurface,(0,0))
    
    def update(self, observable):
        if self.grid:
            self.drawGrid()
        else:
            self.drawBackground()
        for agent in observable.agentList:
            agent.draw(self)
        pygame.display.flip()