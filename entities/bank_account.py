class BankAccount:
    _counter = 0

    def __init__(self, holder, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        BankAccount._counter += 1
        self._BankAccount__number = f"SMART-{BankAccount._counter:04d}"
        self._BankAccount__balance = balance
        self._BankAccount__holder = holder

    @property
    def holder(self):
        return self.__holder
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def number(self):
        return self.__number
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._BankAccount__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._BankAccount__balance < amount:
            from exceptions.errors import InsufficientFundsError
            raise InsufficientFundsError(self._BankAccount__balance, amount)
        self._BankAccount__balance -= amount

    
    def get_info(self):
        return {
            "Holder": self.__holder,
            "Balance": self.__balance,
            "Number": self.__number,
            "Account Class": self.__class__.__name__
        }
    
    def __str__ (self):
        return f"[{self.__class__.__name__}] Account: {self.number} | Holder: {self.holder} | Balance: ${self.balance:,.2f}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(holder='{self.holder}', balance={self.balance})"
    
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self.number == other.number
    