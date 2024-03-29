# Polymorphism (operator overloading)
# When the same operator is allowed to have different meaning according to the context

class ComplexNumbers:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i +", self.img, "j")

    # using dunder functions
    def __add__(self, new_num):
        new_real = self.real + new_num.real
        new_img = self.img + new_num.img
        new_complex_number = ComplexNumbers(new_real, new_img)
        return new_complex_number

    def __sub__(self, new_num):
        new_real = self.real - new_num.real
        new_img = self.img - new_num.img
        new_complex_number = ComplexNumbers(new_real, new_img)
        return new_complex_number

num1 = ComplexNumbers(1,2)
num1.show_number()

num2 = ComplexNumbers(3,4)
num2.show_number()

num3 = num1 - num2
num3.show_number()
