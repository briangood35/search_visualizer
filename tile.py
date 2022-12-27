class Coordinate:
    """Coordinate Class
    """

    def __init__(self, x:int, y:int):
        """Coordinate initializer

        Args:
            x (int): X position in grid
            y (int): Y position in grid
        """

        self.x = x
        self.y = y

class Tile:
    """Tile Class
    """

    parent:Coordinate

    def __init__(self, location:Coordinate):
        """Tile Initializer

        Args:
            x (int): X position in grid
            y (int): Y position in grid
        """
        self.location = location
        self.parent = None
        self.visited = False

    def is_start(self) -> bool:
        """Checks if tile is the start tile

        Returns:
            bool: True if tile is the start tile, false if not
        """
        return self.location.x == 10 and self.location.y == 10

    def is_end(self) -> bool:
        """Checks if tile is the end tile

        Returns:
            bool: True if tile is the end tile, false if not
        """
        return self.location.x == 40 and self.location.y == 35
