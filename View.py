import pygame
from pygame.locals import *

class View:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("S.M.A.")
    
    def drawBackground(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250,250,250))

    def drawGrid(self,resX,resY):
        self.grid = pygame.Surface(self.screen.get_size())
        self.grid = self.grid.convert()
        self.grid.fill((250,250,250,255))

        width = self.grid.get_width()
        height = self.grid.get_height()
        for i in range(0,width, width/resX):
            pygame.draw.line(self.grid, (0,0,0), (i,0), (i,height-1))
    
        for j in range(0,height, height/resY):
            pygame.draw.line(self.grid, (0,0,0), (0,j), (width-1,j))
        self.background.blit(self.grid, (0,0))

    def update(self):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()