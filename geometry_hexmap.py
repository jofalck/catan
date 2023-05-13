
from geometry_hex import Hex


N = 3 # The radius of the map.Rings of hexes outside center hex.
# it is 3 because we need ocean hexes around the map.

class HexMap:
    def __init__(self):
        self.map = self.map_generate()
    
    def map_generate(self):
        """Generate a hex map.

        Returns:
            set: A set of hexes in the map.
        """
        map_set = set()
        for q in range(-N, N+1):
            r1 = max(-N, -q - N)
            r2 = min(N, -q + N)
            for r in range(r1, r2+1):
                map_set.add(Hex(q, r))
        return map_set
    
    def get_hex(self, q, r):
        """Get a hex from the map.

        Args:
            q (int): The q coordinate of the hex.
            r (int): The r coordinate of the hex.
        Returns:
            Hex: The hex at the given coordinates, or None if it does not exist in the map.
        """
        
        for hex in self.map:
            if hex.q == q and hex.r == r:
                return hex
        raise ValueError(f"Hex ({q}, {r}) does not exist in the map.")
    
    def __iter__(self):
        """Iterate over the hexes in the map.

        Yields:
            Hex: The next hex in the map.
        """
        for hex in self.map:
            yield hex
    
    
# tests:
def create_hexmap():
    """Create a hex map.
    """
    hexmap = HexMap()
    return hexmap

def test_retrieve_hex_from_hexmap():
    """Test retrieving a hex from a hex map.
    """
    hexmap = create_hexmap()
    hex = hexmap.get_hex(0, 0)
    if(hex.q == 0 and  hex.r == 0):
        print("Hex retrieved successfully.")
    else:
        print("Hex not retrieved successfully.")
    
test_retrieve_hex_from_hexmap()