# customer class
class Customer:

    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender


# function to pass class object as an argument
def greet(customer):
    customer.name = "Harsh"
    customer.gender = "Male"


# creating a customer class object
cust1 = Customer("Sarika", "Female")
print(cust1.name, cust1.gender)

# calling function pass by reference
greet(cust1)

# values will get updated here
print(cust1.name, cust1.gender)
