from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.transactions = []  # track every transactions
    def __len__(self):
        return len(self.transactions)  # no of transactions
    
    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

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

    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f"Deposited {amount}")
        return f"Hi {self.owner} your savings account has been deposited with {amount}, your balance is {self._balance}"

    def withdraw(self, amount):
        self._balance -= amount
        self.transactions.append(f"withdrawn {amount}")  # record it
        return f"Hi {self.owner},{amount} has been deducted from your savings account, your account balance is {self._balance}"

    def apply_interest(self):
        interest = self._balance * (self.interest_rate/100)
        self._balance += interest

        return f"Hi {self.owner}, your savings account balance after applied interest is {self._balance}"




class CurrentAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f"deposited {amount}")  # record it
        return f"Hi {self.owner}, your curent account has been credited with {amount}, your balance is {self._balance}"

    def withdraw(self, amount):

        self.transactions.append(f"withdrawn {amount}")  # record it
        if self._balance - amount >= -self._overdraft_limit:
            self._balance -= amount
            return f"Hi {self.owner}, {amount} debited successfully, your balance is {self._balance}"
        else:
            return f"Hi {self.owner},withdrawal blocked!! overdraft limit of {self._overdraft_limit} exceeded"

    def check_overdraft(self):

        overdraft_balance = self._balance + self._overdraft_limit

        return f"your overdraft balance is {overdraft_balance}"


print("-----create object from each savings and current account class------")

savings = SavingsAccount("Ebuka", 50000, 5)
savings2 = SavingsAccount("Mubarak", 20000, 10)
current = CurrentAccount("Ebuka", 1000, 3000)

print("-----Testing savings account------")

print(savings.withdraw(500))
print(savings.deposit(500))
print(savings.apply_interest())

print(savings2.withdraw(500))
print(savings2.deposit(500))
print(savings2.apply_interest())


print("-----Testing current account------")

print(current.deposit(1000))
print(current.withdraw(9000))  # exceeds overdraft
print(current.check_overdraft())
print(current.get_balance())

print(len(current))
