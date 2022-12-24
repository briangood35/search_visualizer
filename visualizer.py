
import pygame

class Tile:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x*10+1, (50+y*10)+1, 9, 9)
        self.visited = False

    def is_start(self):
        return self.x == 10 and self.y == 10

    def is_end(self):
        return self.x == 40 and self.y == 35

class Visualizer:
    """Visualization Engine
    """

    # Color definitions
    white = (245, 245, 245)
    black = (51, 51, 51)
    grey = (131, 131, 131)
    green = (45, 200, 105)

    # Tiles map, initialzed to say that all tiles have not been visited
    tiles = []

    def __init__(self, screen_width:int, screen_height:int):
        """Initializes visualization engine

        Args:
            screen_width (int): desired window width
            screen_height (int): desired window height
        """
        pygame.init()
        screen = pygame.display.set_mode([screen_width, screen_height])
        self._init_pygame_screen(screen, screen_width, screen_height)

        for i in range(0, 50):
            row = []
            for j in range(0, 45):
                row.append(Tile(i, j))
            self.tiles.append(row)

        ret = self.user_draw_walls(screen)
        if ret == 1:
            return

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def user_draw_walls(self, screen) -> int:
        """Checks mouse input for clicks and draws walls on map accordingly

        Returns:
            int: Returns 1 if window is closed during this function, returns 0 otherwise
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0]:
                        x, y = pygame.mouse.get_pos()
                        x = x // 10
                        y = (y - 50) // 10
                        if self.tiles[x][y].is_start() or self.tiles[x][y].is_end():
                            continue
                        self.tiles[x][y].visited = True
                        pygame.draw.rect(screen, self.grey, self.tiles[x][y].rect)
                        pygame.display.flip()
                    
                

    def _init_pygame_screen(self, screen, screen_width:int, screen_height:int):
        """Initializes pygame window

        Args:
            screen_width (int): desired window width
            screen_height (int): desired window height
        """
        # Initialize screen
        screen.fill(self.white)
        pygame.draw.line(screen, self.black, (0, 50), (screen.get_width(), 50))

        # BFS and DFS Buttons
        bfs_rect = pygame.Rect(screen_width/6 - 40, 5, 80, 40)
        dfs_rect = pygame.Rect(screen_width*5/6 - 40, 5, 80, 40)
        pygame.draw.rect(screen, self.black, bfs_rect, 4, border_radius=4)
        pygame.draw.rect(screen, self.black, dfs_rect, 4, border_radius=4)

        # BFS and DFS Text
        font = pygame.font.Font(None, 50)
        bfs_text = font.render("BFS", True, self.black)
        dfs_text = font.render("DFS", True, self.black)
        bfs_text_rect = pygame.Rect(screen_width/6 - 35, 10, 70, 30)
        dfs_text_rect = pygame.Rect(screen_width*5/6 - 35, 10, 70, 30)
        screen.blit(bfs_text, bfs_text_rect)
        screen.blit(dfs_text, dfs_text_rect)

        # Reset Button and Text
        reset_rect = pygame.Rect(screen_width/2 - 55, 5, 110, 40)
        pygame.draw.rect(screen, self.black, reset_rect, 4, border_radius=4)
        reset_text = font.render("Reset", True, self.black)
        reset_text_rect = pygame.Rect(screen_width/2 - 48, 10, 100, 30)
        screen.blit(reset_text, reset_text_rect)

        # Draw grid
        for i in range(0, 50):
            pygame.draw.line(screen, self.black, (0, 50+i*10), (screen_width, 50+i*10))
            pygame.draw.line(screen, self.black, (i*10, 50), (i*10, screen_height))

        # Color in start and end tiles
        start = pygame.Rect(101, 151, 9, 9)
        end = pygame.Rect(401, 401, 9, 9)
        pygame.draw.rect(screen, self.green, start, 0)
        pygame.draw.rect(screen, self.green, end, 0)
        
        # Apply changes to window
        pygame.display.flip()


def main():
    Visualizer(500, 500)
    return

if __name__ == "__main__":
    main()
