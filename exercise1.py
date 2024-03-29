"""
Define a Circle class to create a circle with radius r and define methods
to calculate its area and perimeter
"""

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


circle1 = Circle(3)
print(circle1.area())
print(circle1.perimeter())