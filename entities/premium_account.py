from entities.bank_account import BankAccount
from entities.savings_account import SavingsAccount
from exeptions.errors import InsufficientFundsError


class PremiunAccount(BankAccount):
    benefits = ["life insurance", "platinum card", "VIP lounge access"]
    def __init__ (self, holder, balance):
        SavingsAccount.__init__(self, holder, balance)

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError(amount)
        self._BankAccount__balance -= amount

    def show_benefits(self):
        print("=== Premium Account Benefits ===")
        for benefit in self.benefits:
            print(f"-{benefit}")