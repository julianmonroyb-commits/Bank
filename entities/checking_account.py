from entities.bank_account import BankAccount
from exceptions.errors import OverdraftLimitExceeded

class CheckingAccount(BankAccount):
    overdraft_limit = 500000

    def __init__(self, holder, balance):
        super().__init__(holder, balance)

    def withdraw(self, amount):
        if self._BankAccount__balance - amount < -self.overdraft_limit:
            raise OverdraftLimitExceeded(self.overdraft_limit, amount)
        self._BankAccount__balance -= amount
