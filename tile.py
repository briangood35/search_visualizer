class Tile:
    """Tile Class
    """

    def __init__(self, x:int, y:int):
        """Tile Initializer

        Args:
            x (int): X position in grid
            y (int): Y position in grid
        """
        self.x = x
        self.y = y
        self.visited = False

    def is_start(self) -> bool:
        """Checks if tile is the start tile

        Returns:
            bool: True if tile is the start tile, false if not
        """
        return self.x == 10 and self.y == 10

    def is_end(self) -> bool:
        """Checks if tile is the end tile

        Returns:
            bool: True if tile is the end tile, false if not
        """
        return self.x == 40 and self.y == 35
