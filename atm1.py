class Atm:

    def __init__(self) -> None:
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input(
            """
            Hello, how would you like to proceed?
                1. Enter 1 to create pin
                2. Enter 2 to deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check balance
                5. Enter 5 to exit
            """
        )
        if user_input == "1":
            self.create_pin()
        if user_input == "2":
            self.deposit()
        if user_input == "3":
            self.withdraw()
        if user_input == "4":
            self.check_balance()

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")

        self.menu()

    def deposit(self):
        temp = input("Enter you pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit:"))
            self.balance = self.balance + amount
        else:
            print("Invalid pin")

        self.menu()

    def withdraw(self):
        temp = input("Enter you pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            self.balance = self.balance - amount
        else:
            print("Invalid pin")

        self.menu()

    def check_balance(self):
        temp = input("Enter you pin: ")
        if temp == self.pin:
            print("Your balance is: ", self.balance)
        else:
            print("Invalid pin")

        self.menu()


sbi = Atm()
