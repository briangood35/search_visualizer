from graphics import *
import time

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
        self.tiles = []
        for i in range(0, 50):
            row = []
            for j in range(0, 45):
                row.append(Tile(Coordinate(i, j)))
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
                self.bfs()
                return 0
            if self.graphics.buttons['dfs'].collidepoint(pos):
                self.dfs()
                return 0
            # If we clicked somewhere in the menu area that isn't a button, ignore it
            if pos[1] < 50:
                continue
            # Finally, if we clicked a tile, color it
            x = pos[0] // 10
            y = (pos[1] - 50) // 10
            tile = Tile(Coordinate(x, y))
            if not tile.is_start() and not tile.is_end() and not tile.visited:
                self.graphics.color_tile(tile.location, (135, 135, 135))
                self.tiles[x][y].visited = True

    def _out_of_bounds(self, coord:Coordinate) -> bool:
        """Checks if a tile is out of bounds of the grid

        Args:
            tile (Tile): Tile to be checked

        Returns:
            bool: True if tile is out of bounds, False if not
        """
        return coord.x < 0 or coord.x > 49 or coord.y < 0 or coord.y > 44

    def _draw_path(self, tile:Tile):
        """Draws path in blue from tile to the start based on the path taken to get to tile

        Args:
            tile (Tile): Tile to draw path from
        """
        while tile.parent is not None:
            color = (40, 200, 255)
            if tile.is_start() or tile.is_end():
                color = (45, 200, 105)
            self.graphics.color_tile(tile.location, color)
            tile = tile.parent

    def bfs(self) -> int:
        """Breadth first search algorithm starting at (10, 10) and going to (40, 35)

        Returns:
            int: Returns 0 upon finding end tile, 1 if end tile cannot be reached, -1 if pygame window is closed
        """
        queue:list[Tile] = []
        queue.append(self.tiles[10][10])
        self.tiles[10][10].visited = True
        coords = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        while len(queue) != 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return -1
            current = queue[0]
            queue.pop(0)
            if current.is_end():
                self._draw_path(current)
                return 0
            for coord in coords:
                next_tile = Coordinate(current.location.x + coord[0], current.location.y + coord[1])
                if self._out_of_bounds(next_tile) or self.tiles[next_tile.x][next_tile.y].visited:
                    continue
                queue.append(self.tiles[next_tile.x][next_tile.y])
                self.tiles[next_tile.x][next_tile.y].visited = True
                self.tiles[next_tile.x][next_tile.y].parent = current
            self.graphics.color_tile(current.location, (230, 100, 100))
        self._draw_path(current)
        return 1

    def dfs(self):
        """Depth first search algorithm starting at (10, 10) and going to (40, 35)

        Returns:
            int: Returns 0 upon finding end tile, 1 if end tile cannot be reached, -1 if pygame window is closed
        """
        stack:list[Tile] = []
        stack.append(self.tiles[10][10])
        self.tiles[10][10].visited = True
        coords = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        while len(stack) != 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return -1
            current = stack[len(stack) - 1]
            stack.pop()
            if current.is_end():
                self._draw_path(current)
                return 0
            for coord in coords:
                next_tile = Coordinate(current.location.x + coord[0], current.location.y + coord[1])
                if self._out_of_bounds(next_tile) or self.tiles[next_tile.x][next_tile.y].visited:
                    continue
                stack.append(self.tiles[next_tile.x][next_tile.y])
                self.tiles[next_tile.x][next_tile.y].visited = True
                self.tiles[next_tile.x][next_tile.y].parent = current
            self.graphics.color_tile(current.location, (230, 100, 100))
        self._draw_path(current)
        return 1

    def run(self):
        """Search Visualization Controller
        """
        ret = 0
        while not ret:
            self.reset()
            ret = self.draw_walls()
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        return
                pos = self._check_click()
                if self.graphics.buttons['reset'].collidepoint(pos):
                    break

