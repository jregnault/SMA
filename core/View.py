import pygame

class View:
    
    def __init__(self, environment, boxSize=1, backgroundColor=(0,0,0), grid=False):
        self.environement = environment
        self.boxSize = boxSize
        self.grid = grid

        canvasSizeX = environment.gridSizeX * boxSize
        canvasSizeY = environment.gridSizeY * boxSize
        if grid:
            canvasSizeX += environment.gridSizeX + 1
            canvasSizeY += environment.gridSizeY + 1
            
        pygame.init()
        self.screen = pygame.display.set_mode((canvasSizeX,canvasSizeY))
        pygame.display.set_caption("Multi-Agent System")