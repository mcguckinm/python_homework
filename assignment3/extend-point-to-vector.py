import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def euclidean_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
class Vector(Point):
    def __str__(self):
        return f"<{self.x}, {self.y}>"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    


#test code
p1 = Point(3, 4)
p2 = Point(1,4)
print(p1)  # Output: (3, 4)
print(p2)  # Output: (1, 4)
print(p1 == p2)  # Output: False
print(p1.euclidean_distance(p2))  # Output: 2.0


#vectors
print("\nVectors") 
v1 = Vector(3, 4)
v2 = Vector(1, 4)
print(v1)  # Output: <3, 4>
print(v2)  # Output: <1, 4>
v3=v1+v2
print("v1 + v2 =", v3)  # Output: <4, 8>