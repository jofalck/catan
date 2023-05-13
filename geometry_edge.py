

from .geometry_vertex import Vertex


class Edge:
    def __init__ (self, start:Vertex, end:Vertex):
        self.start = start
        self.end = end
        self.hasRoad = False
        
    def __eq__(self, other):
        """Equality operator for edges. Checks both directions. 

        Args:
            other (Edge): The other edge to compare to.

        Returns:
            bool: True if the edges are equal, False otherwise.
        """
        return (self.start == other.start and self.end == other.end) or (self.start == other.end and self.end == other.start)