class BankAccount:
    def __init__(self, account, balance) -> None:
        self._account = account
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount("12345678", 1000000)
print(account._account)
print(account.get_balance())