# Parent class
class Product:
    def review(self):
        print("Product customer review")


# Sub Parent class
class Phone(Product):
    print("Initializing oject from sub parent class")

    def __init__(self, price, brand) -> None:
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")


# Child class
class Smartphone(Phone):
    print("Initializing object from child class")


s = Smartphone(20000, "Apple")
p = Phone(10000, "Samsung")

s.buy()
s.review()
p.review()
