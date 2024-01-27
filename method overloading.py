class Geometry:

    def area(self, a, b=0):
        if b == 0:
            print("Area of circle:", 3.14*a*a)
        else:
            print("Area of rectangle:", a*b)


obj = Geometry()
obj.area(4)
obj.area(4, 5)
