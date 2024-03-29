"""
Create a class Order which stores item and its price
User Dunder function __gt__() to convey that
    order1 > order2 if price of order1 > price of order2
"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        if self.price > order2.price:
            return True
        else:
            return False

order1 = Order("tea", 35)
order2 = Order("sandwich", 30)
print(order1 > order2)