from geometry_hex import Hex


class Vertex:
    """A vertex on the board. It has a q and r coordinate and a direction (N or S) 
    to indicate whether it is the northern or southern vertex of the hex.
    """
    def __init__(self, q:int, r:int, direction:str):
        self.q = q
        self.r = r
        self.direction = direction # N or S
        self.has_settlement = False
        self.has_city = False
        self.has_port = False # a player can store locally the port they have access to
        self.port = None
        self.id = f"{q},{r},{direction}"

    def __repr__(self):
        return f"Vertex({self.q}, {self.r}, {self.direction})"
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)
    
    def touched_hexes(self):
        """Returns the hexes that touch this vertex.

        Returns:
            list: The hexes that touch this vertex.
        """
        if self.direction == "N":
            return [Hex(self.q, self.r-1), 
                    Hex(self.q+1, self.r), 
                    Hex(self.q, self.r)]
        elif self.direction == "S":
            return [Hex(self.q, self.r), 
                    Hex(self.q-1, self.r+1), 
                    Hex(self.q, self.r+1)]
        
    def adjacent_vertices(self):
        """Returns the vertices that are adjacent to this vertex.

        Returns:
            list: The vertices that are adjacent to this vertex.
        """
        if self.direction == "N":
            return [Vertex(self.q+1, self.r-2, "S"),
                    Vertex(self.q, self.r-1, "N"),
                    Vertex(self.q+1, self.r-1, "S")]
        elif self.direction == "S":
            return [Vertex(self.q-1, self.r+1, "N"),
                    Vertex(self.q, self.r+1, "S"),
                    Vertex(self.q-1, self.r+2, "N")]
    