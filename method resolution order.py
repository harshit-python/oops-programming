# Parent class 1
class Phone():

    def __init__(self, price, brand, camera) -> None:
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


# Parent class 2
class Product:
    def buy(self):
        print("Buying a product")


# Child class
class Smartphone(Product, Phone):
    print("Initializing object from child class")


s = Smartphone(20000, "Apple", 13)
s.buy()
