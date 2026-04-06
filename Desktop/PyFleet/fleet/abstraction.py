from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property  # getter
    def balance(self):
        return f"{self._balance}"

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return f"your account balance is {self._balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"SAVINGS = Owner: {self.owner} | Balance: {self._balance} | overdraft_limit: {self.interest_rate}%"

    def deposit(self, amount):
        self._balance += amount
        return f"your savings account has been deposited with {amount}, your balance is {self._balance}"

    def withdraw(self, amount):
        self._balance -= amount
        return f"{amount} has been deducted from your savings account, your account balance is {self._balance}"

    def apply_interest(self):
        interest = self._balance * (self.interest_rate/100)
        self._balance += interest

        return f"your savings account balance after applied interest is {self._balance}"


class CurrentAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def __str__(self):
        return f" CURRENT = Owner: {self.owner} | Balance: {self._balance} | overdraft_limit: {self._overdraft_limit}"

    def deposit(self, amount):
        self._balance += amount
        return f"your curent account has been credited with {amount}, your balance is {self._balance}"

    def withdraw(self, amount):
        if self._balance - amount >= -self._overdraft_limit:
            self._balance -= amount
            return f"{amount} debited successfully, your balance is {self._balance}"
        else:
            return f"withdrawal blocked!! overdraft limit of {self._overdraft_limit} exceeded"

    def check_overdraft(self):

        overdraft_balance = self._balance + self._overdraft_limit

        return f"your overdraft balance is {overdraft_balance}"


print("-----create object from each savings and current account class------")

savings = SavingsAccount("Ebuka", 50000, 5)
current = CurrentAccount("Ebuka", 1000, 3000)

print(current)
print(savings)
