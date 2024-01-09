class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    # method to print fraction
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    # method to add two fractions
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

    # method to subtract two fractions
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

    # method to multiple two fractions
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

    # method to divide two fractions
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return "{}/{}".format(temp_num, temp_den)



x = Fraction(3, 4)
y = Fraction(5, 6)
print("Addition:", x+y)
print("Subtraction:", x-y)
print("Multiplication:", x*y)
print("Division:", x/y)