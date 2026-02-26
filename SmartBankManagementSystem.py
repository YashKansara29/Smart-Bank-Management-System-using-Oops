class BankAccount:

    def __init__(self, account_number, account_holder, _balance):
        # Initialize account details
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = _balance

    def deposit(self, amount):
        # Add amount to balance
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        # Deduct amount if sufficient balance
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

    def get_balance(self):
        # Return current balance
        return self._balance

    def calculate_interest(self):
        # Default 5% interest
        return self._balance * 0.05
    

class SavingsAccount(BankAccount):

    def __init__(self, intrest_rate, minimum_balance, account_number, account_holder, _balance):
        # Initialize savings account with extra attributes
        super().__init__(account_number, account_holder, _balance)
        self.intrest_rate = intrest_rate
        self.minimum_balance = minimum_balance

    def calculate_interest(self):
        # Calculate interest using savings rate
        return self._balance * self.intrest_rate

    def check_minimum_balance(self):
        # Check if balance meets minimum requirement
        if self._balance < self.minimum_balance:
            print("Balance is below the minimum required balance.")
        else:
            print("Balance meets the minimum required balance.")

    def withdraw(self, amount):
        # Ensure balance does not go below minimum
        if self._balance - amount < self.minimum_balance:
            print("Cannot withdraw. Balance would fall below the minimum required balance.")
        else:
            super().withdraw(amount)


class CurrentAccount(BankAccount):

    def __init__(self, overdraft_limit, account_number, account_holder, _balance):
        # Initialize current account with overdraft limit
        super().__init__(account_number, account_holder, _balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Allow withdrawal within overdraft limit
        if amount > self._balance + self.overdraft_limit:
            print("Cannot withdraw. Amount exceeds balance and overdraft limit.")
        else:
            super().withdraw(amount)


# Example usage
savings_account = SavingsAccount(
    intrest_rate=0.05,
    minimum_balance=500,
    account_number="123456789",
    account_holder="John Doe",
    _balance=1000
)

savings_account.deposit(200)
savings_account.withdraw(300)
savings_account.check_minimum_balance()
print(f"Interest earned: {savings_account.calculate_interest()}")

current_account = CurrentAccount(
    overdraft_limit=500,
    account_number="987654321",
    account_holder="Jane Doe",
    _balance=1000
)

current_account.deposit(500)
current_account.withdraw(1200)
print(current_account.calculate_interest())