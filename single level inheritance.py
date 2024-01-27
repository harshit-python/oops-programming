# Parent class
class Phone:

    def __init__(self, price, brand) -> None:
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")


# Child class
class Smartphone(Phone):

    def buy(self):
        print("Buying a smartphone")


s = Smartphone(20000, "Apple")
print(s.price)
print(s.brand)
s.buy()
