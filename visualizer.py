
import pygame




class Visualizer:
    """Visualization Engine
    """

    # Color definitions
    white = (245, 245, 245)
    black = (51, 51, 51)

    def _init_pygame_screen(self, screen_width:int, screen_height:int):
        """Initializes pygame window

        Args:
            screen_width (int): desired window width
            screen_height (int): desired window height
        """
        # Initialize screen
        pygame.init()
        screen = pygame.display.set_mode([screen_width, screen_height])
        screen.fill(self.white)
        pygame.draw.line(screen, self.black, (0, 50), (screen.get_width(), 50))

        # BFS and DFS Buttons
        bfs_rect = pygame.Rect(screen_width/4 - 40, 5, 80, 40)
        dfs_rect = pygame.Rect(screen_width*3/4 - 40, 5, 80, 40)
        pygame.draw.rect(screen, self.black, bfs_rect, 4, border_radius=4)
        pygame.draw.rect(screen, self.black, dfs_rect, 4, border_radius=4)

        # BFS and DFS Text
        font = pygame.font.Font(None, 50)
        bfs_text = font.render("BFS", True, self.black)
        dfs_text = font.render("DFS", True, self.black)
        bfs_text_rect = pygame.Rect(screen_width/4 - 35, 10, 70, 30)
        dfs_text_rect = pygame.Rect(screen_width*3/4 - 35, 10, 70, 30)
        screen.blit(bfs_text, bfs_text_rect)
        screen.blit(dfs_text, dfs_text_rect)

        # Draw grid
        for i in range(0, 50):
            pygame.draw.line(screen, self.black, (0, 50+i*10), (screen_width, 50+i*10))
            pygame.draw.line(screen, self.black, (i*10, 50), (i*10, screen_height))
        
        # Apply changes to window
        pygame.display.flip()

    def __init__(self, screen_width:int, screen_height:int):
        """Initializes visualization engine

        Args:
            screen_width (int): desired window width
            screen_height (int): desired window height
        """
        
        self._init_pygame_screen(screen_width, screen_height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return




def main():
    Visualizer(500, 500)
    return

if __name__ == "__main__":
    main()
