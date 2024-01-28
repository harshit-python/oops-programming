class Bank:
    def __init__(self) -> None:
        self.customers = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")

        else:
            print("Account number does not exists.")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exists.")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print("Your account balance is:", balance)

        else:
            print("Account number does not exists.")


bank = Bank()
account1 = "SB-123"
amount1 = 100000
bank.create_account(account1)
bank.check_balance(account1)
bank.make_deposit(account1, amount1)
bank.check_balance(account1)
bank.make_withdrawal(account1, 25000)
bank.check_balance(account1)
