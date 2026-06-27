class BancoError(Exception):
    pass

class InsufficientFundsError(BancoError):
    def __init__ (self, current_balance, requested_amount):
        self.current_balance = current_balance
        self.requested_amount = requested_amount
        message = f"Insufficient funds. Available: {current_balance}, Requested: {requested_amount}"
        super().__init__(message)

class OverdraftLimitExeceeded(BancoError):
    def __init__(self, limit, requested_amount):
        self.limit = limit
        self.requested_amount = requested_amount
        message = f"Overdraft limit exceeded. Limit: {limit}, Requested: {requested_amount}"
        super().__init__(message)

class AccountNotFoundError(BancoError):
    def __init__(self, searched_number):
        self.searched_number = self.searched_number
        message = f"Account {searched_number} was not found"
        super().__init___(message)

class InvalidTransferError(BancoError):
    def __init__(self, message = f"Invalid Transfer Error"):
        super().__init__(message)

