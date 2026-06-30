from entities.bank_account import BankAccount
from exceptions.errors import AccountNotFoundError, InvalidTransferError

class Bank:
    def __init__(self):
        self._accounts = {}

    def add_account(self, account):
        if not isinstance(account, BankAccount):
            raise TypeError("Must be a valid BankAccount instance")
        
        self._accounts[account.number] = account

    def find_account(self, number):
        if number not in self._accounts:
            raise AccountNotFoundError(number)
        return self._accounts[number]

    def transfer(self, origin_num, destination_num, amount):
        assert origin_num != destination_num, "Cannot transfer to the same account"
        
        try:
            origin = self.find_account(origin_num)
            destination = self.find_account(destination_num)
            origin.withdraw(amount)
            destination.deposit(amount)
            
        except Exception as e:
            raise InvalidTransferError(f"Transfer failed: {str(e)}") from e
        else:
            print("Transfer successful")
        finally:
            print("Transfer operation completed")

    def get_accounts_above_balance(self, threshold):
        return list(filter(lambda c: c.balance > threshold, self._accounts.values()))

    def get_formatted_balances(self):
        return list(map(lambda c: f"{c.number}: ${c.balance:,.0f}", self._accounts.values()))

    def get_balance_ranking(self):
        return sorted(self._accounts.values(), key=lambda c: c.balance, reverse=True)

    def generate_report(self):
        yield "=== SMART BANK REPORT ==="
        yield f"Total accounts: {len(self._accounts)}"
        for account in self._accounts.values():
            yield str(account)
        yield "=== END OF REPORT ==="

