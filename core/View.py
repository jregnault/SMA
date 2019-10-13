import pygame

class View:
    
    def __init__(self, environment, boxSize=1, backgroundColor=(0,0,0), grid=False):
        self.environment = environment
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
        self.screen.fill(backgroundColor)
        if grid:
            self.drawGrid()
    
    def drawGrid(self):
        """Add a grid to the view."""
        gridSurface = pygame.Surface(self.screen.get_size())
        gridSurface = gridSurface.convert_alpha()
        gridSurface.fill(0,0,0,0)

        width = gridSurface.get_width()
        height = gridSurface.get_height()
        for i in range(0, self.environment.width+1):
            pos = i * self.boxSize + i
            pygame.draw.line(gridSurface, (0,0,0,255), (pos,0), (pos,height-1))
        
        for j in range(0, self.environment.height+1):
            pos = j * self.boxSize + j
            pygame.draw.line(gridSurface, (0,0,0,255), (0,pos), (width-1,pos))
        
        self.screen.blit(gridSurface)
    
    def update(self, observable):
        for agent in observable.agentList:
            agent.draw(self.screen)
        pygame.display.flip()