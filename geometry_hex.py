"""Hex class and helper functions."""

class Hex:
    def __init__(self, q, r):
        self.q = q
        self.r = r
        
    def __add__(self, other):
        """Add two hexes together.
        
        Args:
            other (Hex): The other hex to add to this one.
        Returns:
            Hex: The sum of the two hexes.
        """
        return Hex(self.q + other.q, self.r + other.r)
    
    def __sub__(self, other):
        """Subtract two hexes.

        Args:
            other (Hex): The other hex to subtract from this one.

        Returns:
            Hex: The difference of the two hexes.
        """
        return Hex(self.q - other.q, self.r - other.r)
    
    def scale(self, k):
        """Scale a hex by a constant.

        Args:
            k (int): The constant to scale the hex by.

        Returns:
            Hex: The scaled hex.
        """
        return Hex(self.q * k, self.r * k)
    
    def direction(self, direction):
        """Get the direction of a hex.

        Args:
            direction (int): The direction to get the hex in.

        Returns:
            Hex: The hex in the given direction.
        """
        return hex_directions[direction]
    
    def neighbor(self, direction):
        """Get the neighbor of a hex in a given direction.

        Args:
            direction (int): The direction to get the neighbor in. 

        Returns:
            Hex: The neighbor in the given direction.
        """
        return self + self.direction(direction)
    
    def __str__(self):
        return f"Hex({self.q}, {self.r})"
    
    def __repr__(self):
        return f"{self.q},{self.r}"
    
    def __eq__(self, other):
        """Check if two hexes are equal.

        Args:
            other (Hex): The other hex to compare to.

        Returns:
            bool: Whether the two hexes are equal.
        """
        return self.q == other.q and self.r == other.r
    
    def __hash__(self):
        return hash((self.q, self.r))
    
hex_directions = [Hex(1, 0), Hex(1, -1), Hex(0, -1), Hex(-1, 0), Hex(-1, 1), Hex(0, 1)]