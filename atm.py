class ATM:

    # constructor # special/magic/dunder methods
    #  self is the current object on which we are working
    def __init__(self):
        # using __ to hide the data from external user (encapsulation)
        self.__pin = ""
        self.__balance = 0
        # calling menu method
        self.menu()

    # getter method
    def get_pin(self):
        return self.__pin

    # setter method
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed")
        else:
            print("Not allowed")

    def menu(self):
        user_input = str(input("""
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
        """))

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successfully")

        self.menu()

    def deposit(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
        else:
            print("Invalid pin")

        self.menu()

    def withdraw(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount < self.balance:
                self.__balance = self.__balance - amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")

        self.menu()

    def check_balance(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Invalid pin")

        self.menu()


sbi = ATM()
