class Phone:

    def __init__(self, price, brand, camera):
        self.price = price
        self.__brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Smartphone(Phone):

    # creating method with same
    def buy(self):
        print("Buying a smartphone")


s = Smartphone(20000, "Apple", 13)

# This will call buy method from Smartphone child class
s.buy()
