from tile import *
import pygame as pg


class Graphics:
    """Pygame Graphics Controller
    """

    buttons = {}
    screen:pg.Surface

    # Screen size
    width = 500
    height = 500

    # Color definitions
    white = (245, 245, 245)
    black = (51, 51, 51)
    grey = (131, 131, 131)
    green = (45, 200, 105)

    def __init__(self):
        """Creates pygame window and draws buttons and grid
        """
        pg.init()
        self.screen = pg.display.set_mode([self.width, self.height])
        # Initialize screen
        self.screen.fill(self.white)
        pg.draw.line(self.screen, self.black, (0, 50), (self.width, 50))

        # BFS and DFS Buttons
        bfs_rect = pg.Rect(self.width/6 - 40, 5, 80, 40)
        dfs_rect = pg.Rect(self.width*5/6 - 40, 5, 80, 40)
        pg.draw.rect(self.screen, self.black, bfs_rect, 4, border_radius=4)
        pg.draw.rect(self.screen, self.black, dfs_rect, 4, border_radius=4)
        self.buttons['bfs'] = bfs_rect
        self.buttons['dfs'] = dfs_rect

        # BFS and DFS Text
        font = pg.font.Font(None, 50)
        bfs_text = font.render("BFS", True, self.black)
        dfs_text = font.render("DFS", True, self.black)
        bfs_text_rect = pg.Rect(self.width/6 - 35, 10, 70, 30)
        dfs_text_rect = pg.Rect(self.width*5/6 - 35, 10, 70, 30)
        self.screen.blit(bfs_text, bfs_text_rect)
        self.screen.blit(dfs_text, dfs_text_rect)

        # Reset Button and Text
        reset_rect = pg.Rect(self.width/2 - 55, 5, 110, 40)
        pg.draw.rect(self.screen, self.black, reset_rect, 4, border_radius=4)
        reset_text = font.render("Reset", True, self.black)
        reset_text_rect = pg.Rect(self.width/2 - 48, 10, 100, 30)
        self.buttons['reset'] = reset_rect
        self.screen.blit(reset_text, reset_text_rect)

        # Draw grid
        for i in range(0, 50):
            pg.draw.line(self.screen, self.black, (0, 50+i*10), (self.width, 50+i*10))
            pg.draw.line(self.screen, self.black, (i*10, 50), (i*10, self.height))

        # Color in start and end tiles
        start = pg.Rect(101, 151, 9, 9)
        end = pg.Rect(401, 401, 9, 9)
        pg.draw.rect(self.screen, self.green, start)
        pg.draw.rect(self.screen, self.green, end)
        
        # Apply changes to window
        pg.display.flip()

    def color_tile(self, tile:Tile, color:pg.Color):
        """Colors tile located in grid at (x, y)

        Args:
            x (int): X position of tile in grid
            y (int): Y position of tile in grid
            color (pg.Color): RGB color
        """
        rect = pg.Rect(tile.x*10+1, tile.y*10+51, 9, 9)
        pg.draw.rect(self.screen, color, rect)
        pg.display.flip()
