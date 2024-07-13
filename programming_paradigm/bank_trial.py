import unittest 
import re


class BankAccount:
    def __init__(self, amount):
        self.account_balance = 0
        self.amount = amount 
        

    def deposit(self,amount):
        self.account_balance += amount
        return f'Deposited: ${self.account_balance}'
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f'Withdrew: ${amount}'
        else:
            return f'Insufficient funds.'
        
    def display_balance(self):  
         return f"Current Balance: ${self.account_balance}"


operation = BankAccount(100)

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        result = operation.deposit(50)
        self.assertEqual(result,'Deposited: $50')
    def test_withdraw(self):
        result = operation.withdraw(20)
        self.assertEqual(result, 'Withdrew: $20')

    def test_insufficient_withdraw(self):
        result = operation.withdraw(150)
        self.assertEqual(result, 'Insufficient funds.')

    def test_display_balance(self):
        result = operation.display_balance()
        self.assertEqual(result, 'Current Balance: $50')

if __name__ == "__main__":
    unittest.main()
