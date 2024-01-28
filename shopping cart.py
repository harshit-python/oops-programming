class ShoppingCart:

    def __init__(self) -> None:
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        return len(self.items)


cart = ShoppingCart()
cart.add_item("Apple", 100)
cart.add_item("Mango", 200)
cart.add_item("Banana", 150)
print("Current items in cart:")
for item in cart.items:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)
cart.remove_item("Banana")
print("Items after removing Banana:")
for item in cart.items:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)
