class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    # method to update profile which internally calls change_address() method
    def edit_profile(self, new_name, new_city, new_pincode, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pincode, new_state)


class Address:

    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    # method to change address
    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state


add = Address("Sitarganj", 262405, "Uttarakhand")
cust = Customer("Harsh", "Male", add)

print(cust.address.city)

# updating address
cust.edit_profile("Shailesh", "Ramnagar", 244715, "Uttarakhand")

print(cust.address.city)
