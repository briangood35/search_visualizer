from graphics import *

class Search:
    """Search Driver
    """

    tiles = []
    graphics:Graphics

    def __init__(self):
        """Initializes visualization engine
        """
        self.reset()

    def reset(self):
        """Reset the window to original state
        """
        for i in range(0, 50):
            row = []
            for j in range(0, 45):
                row.append(Tile(i, j))
            self.tiles.append(row)

        self.graphics = Graphics()
        pg.event.clear()

    def _check_click(self) -> tuple[int, int]:
        """Checks for click in pygame window

        Returns:
            tuple[int, int]: (-1, -1) on QUIT, (0, -1) when no click detected, otherwise returns click position
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return (-1, -1)
            if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEMOTION:
                mouse_buttons = pg.mouse.get_pressed()
                if mouse_buttons[0]:
                    return pg.mouse.get_pos()
        return (0, -1)

    def draw_walls(self) -> int:
        """User draws walls on grid, then presses a button to start a search or reset the grid

        Returns:
            int: Returns 1 on QUIT, 0 on successful exit
        """
        while True:
            pos = self._check_click()
            # check if we quit the pygame window
            if pos == (-1, -1):
                return 1
            # if we didn't click anything, continue
            if pos == (0, -1):
                continue
            # check buttons
            if self.graphics.buttons['reset'].collidepoint(pos):
                self.reset()
            if self.graphics.buttons['bfs'].collidepoint(pos):
                # self.bfs()
                print("dfs")
                return 0
            if self.graphics.buttons['dfs'].collidepoint(pos):
                # self.dfs()
                print("dfs")
                return 0
            # If we clicked somewhere in the menu area that isn't a button, ignore it
            if pos[1] < 50:
                continue
            # Finally, if we clicked a tile, color it
            x = pos[0] // 10
            y = (pos[1] - 50) // 10
            tile = Tile(x, y)
            if not tile.is_start() and not tile.is_end() and not tile.visited:
                self.graphics.color_tile(tile, (135, 135, 135))
                self.tiles[x][y].visited = True
