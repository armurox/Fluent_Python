import math

class Vector:
    def __init__(self, x, y):
        if type(x) != type(y):
            raise TypeError('The elements of the vector do not have the same type!')
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    

class Line:
    def __init__(self, v, u):
        self.v = v
        self.u = u
    
    def size(self):
        return abs(self.v - self.u)
