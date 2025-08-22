class Vector2D:
    def __init__(self, d):
        if isinstance(d, int):
            # Example: Vector2D(3) -> [0, 0, 0]
            self._coords = [0] * d
        else:
            # Example: Vector2D([1,2,3]) -> [1, 2, 3]
            self._coords = list(d)
    
    def __len__(self):
        return len(self._coords)
        # We can access elements like a list
    def __getitem__(self,i):
        return self._coord[i]
        # For accessing index[i] values
    def __setitem__(self,i,val):
        self._coord[i]=val
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return Vector2D([a + b for a, b in zip(self._coords, other._coords)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return Vector2D([a - b for a, b in zip(self._coords, other._coords)])

            # Negation
    def __neg__(self):  # negation: -a
        return Vector2D([-x for x in self._coords])

    def __mul__(self, scalar):   # scalar multiplication a*3
        return Vector2D([x * scalar for x in self._coords])

    def __rmul__(self, scalar):  # scalar multiplication 3*a
        return self * scalar
    def __xor__(self, other):    # dot product (a^b)
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        return sum(a * b for a, b in zip(self._cord, other._coords))    
    
    def __str__(self):
        return str(self._coords)

                  



   