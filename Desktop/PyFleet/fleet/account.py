class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        # underscore for encapsulation making it an internal convention
        self._balance = float(balance)

    @property
    def balance(self):  # read-only view by default
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


acct = Account("Ayo", 200000)
acct.withdraw(150000)
print(acct.balance)
