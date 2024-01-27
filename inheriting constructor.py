class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera


class Smartphone(Phone):
    pass


s = Smartphone(20000, "Apple", 13)
# this object will inerit constructor from parent class since it does not have its default constructor
print(s.price)
print(s.camera)

# this will throw error since we are inheriting private member from parent class
try:
    print(s.__brand)
except Exception as e:
    print(e)
