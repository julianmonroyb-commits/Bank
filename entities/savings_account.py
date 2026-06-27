from entities.bank_account import BankAccount
from exeptions.errors import InsufficientFundsError

class SavingsAccount(BankAccount):
    interest_rate = 0.03
    def __init__ (self, holder, balance):
        super().__init__ (holder, balance )

    def withdraq(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError(self.balance, amount)
        
    def interest_account(self):
        interest = self.balace * self.interest_rate
        self.deposit(interest)

