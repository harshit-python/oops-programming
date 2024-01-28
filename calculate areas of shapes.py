# program to create shape class. Includes message for finding area of circle, triangle and square.

class Shape:

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        return area

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3) -> None:
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        return area

    def calculate_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter


class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        return perimeter


# creating a circle and calculating its area and perimeter
circle1 = Circle(7)
print("Area of circle is:", circle1.calculate_area())
print("Perimeter of circle is:", circle1.calculate_perimeter())

# creating a rectangle and calculating its area and perimeter
rectangle1 = Rectangle(5, 7)
print("Area of Rectangle is:", rectangle1.calculate_area())
print("Perimter of Rectangle is:", rectangle1.calculate_perimeter())

# creating a triangle and calculating its area and perimeter
triangle1 = Triangle(5, 4, 4, 3, 5)
print("Area of Triangle is:", triangle1.calculate_area())
print("Perimeter of Triangle is:", triangle1.calculate_perimeter())
