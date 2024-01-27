# customer class
class Customer:

    # constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # __str__ method to print name while we call and print object
    def __str__(self) -> str:
        return self.name

    def intro(self):
        print("I am", self.name, "and I am", self.age)


cust1 = Customer("Harsh", 25)
cust2 = Customer("Sarika", 22)

list1 = [cust1, cust2]
for i in list1:
    i.intro()
