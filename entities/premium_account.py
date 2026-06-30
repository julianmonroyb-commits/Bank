from entities.bank_account import BankAccount
from security.audit import AuditMixin
from exceptions.errors import InsufficientFundsError 

class PremiumAccount(BankAccount, AuditMixin):
    benefits = ["life insurance", "platinum card", "VIP lounge access"]
    
    def __init__(self, holder, balance):
        BankAccount.__init__(self, holder, balance)
        AuditMixin.__init__(self)

    def withdraw(self, amount):
        if self._BankAccount__balance < amount:
            raise InsufficientFundsError(self._BankAccount__balance, amount)
        self._BankAccount__balance -= amount

    def show_benefits(self):
        print("=== Premium Account Benefits ===")
        for benefit in self.benefits:
            print(f"- {benefit}")
