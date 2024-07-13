class BankAccount:
    def __init__(self,amount ):
        self.account_balance = 0
        self.amount = amount

    def deposit(self, amount):
        self.account_balance += self.amount
        return f'Deposited: ${self.account_balance}'
    
    def withdraw(self,amount):
        if amount < self.account_balance:
            self.account_balance -= self.amount
            return f'Withdrew: ${self.account_balance}'
        else:
            return f'Insufficient funds'
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")


