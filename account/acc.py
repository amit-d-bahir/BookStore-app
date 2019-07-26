
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()



account_obj = Account("balance.txt")
print(account_obj.balance)
account_obj.deposit(500)
print(account_obj.balance)
