# Parent class
class Phone():

    def __init__(self, price, brand) -> None:
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")


# Child class 1
class SmartPhone(Phone):
    print("Initializing object from child class 1")


# Child class 2
class FeaturePhone(Phone):
    print("Initializing object from child class 2")


s = SmartPhone(20000, "Apple")
f = FeaturePhone(10000, "Samsung")

s.buy()
f.buy()
