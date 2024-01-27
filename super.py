class Phone:

    # constuctor for Phone class
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera


class Smartphone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        # calling constructor from parent class Phone using super()
        # this should always be the first statement inside constructor
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")


# creating Smartphone object
s = Smartphone(20000, "Apple", 13, "iOS", 8)

# This will call buy method from Smartphone child class
print(s.os)
print(s.price)
try:
    # trying to call private data from parent class
    print(s.__brand)
except Exception as e:
    print(e)
