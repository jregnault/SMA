import pygame

from core.Environment import Environment


class View:
    """Represents the window view to have a graphic representation of the simulation."""
    
    def __init__(self, environment: Environment, box_size: int = 1, grid: bool = False) -> None:
        """Creates a new view
        Parameters:
            environment: the environment to graphically represent
            box_size: the size in pixels of a cell
            grid: whether to show the grid on the view
        """
        self.environment = environment
        self.boxSize = box_size
        self.grid = grid

        canvas_size_x = environment.width * box_size
        canvas_size_y = environment.height * box_size
        if grid:
            canvas_size_x += environment.width + 1
            canvas_size_y += environment.height + 1

        pygame.init()
        self.screen = pygame.display.set_mode((canvas_size_x, canvas_size_y))
        pygame.display.set_caption("Multi-Agent System")
        self.draw_background()
        if grid:
            self.draw_grid()
    
    def draw_background(self) -> None:
        """Draws the environment background on the screen."""
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(self.environment.color)
        self.screen.blit(background, (0, 0))

    def draw_grid(self) -> None:
        """Draws the grid on the screen."""
        grid_surface = pygame.Surface(self.screen.get_size())
        grid_surface = grid_surface.convert()
        grid_surface.fill(self.environment.color)

        width = grid_surface.get_width()
        height = grid_surface.get_height()
        for i in range(0, self.environment.width+1):
            pos = i * self.boxSize + i
            pygame.draw.line(grid_surface, (0, 0, 0, 255), (pos, 0), (pos, height-1))
        
        for j in range(0, self.environment.height+1):
            pos = j * self.boxSize + j
            pygame.draw.line(grid_surface, (0, 0, 0, 255), (0, pos), (width-1, pos))
        
        self.screen.blit(grid_surface, (0, 0))
    
    def update(self) -> None:
        """Renders the current state of the view on screen."""
        if self.grid:
            self.draw_grid()
        else:
            self.draw_background()
        for y in range(0, self.environment.height):
            for x in range(0, self.environment.width):
                agent = self.environment.get(x, y)
                if agent is not None:
                    agent.draw(self)
        pygame.display.flip()
