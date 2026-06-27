from entities.bank_account import BankAccount
from exeptions.errors import OverdraftLimitExeceeded

class ChekingAccount(BankAccount):
    overdraf_limit = 500000
    def __init__ (self, holder, balance):
        super().__init__ (holder, balance)

    def withdraw(self, amount):
        if self.balance - amount < self.overdraf_limit:
            raise OverdraftLimitExeceeded
        