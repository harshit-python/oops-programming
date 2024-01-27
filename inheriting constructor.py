class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera


class Smartphone(Phone):
    pass


s = Smartphone(20000, "Apple", 13)
# this object will inerit constructor from parent class since it does not have its default constructor
print(s.brand)
print(s.price)
print(s.camera)
