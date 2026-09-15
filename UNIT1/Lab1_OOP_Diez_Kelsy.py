
class notebook:
    def __init__(self, Numhojas, color, size):
        self.Numhojas = Numhojas
        self.color = color
        self.size = size

    def write (self):
            print ("Write on the notebook")

    def description (self):
            print (f"The notebook has {self.Numhojas} pages")

#create multiple instances using the class "Table"

notebook1 = notebook("100","white","B1")
notebook2 = notebook("50", "blue","A2")

print (notebook1.size)

notebook1.description()
notebook2.description()


class BankAccount:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.balance = initial_balance 

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(f"{self.holder}'s balance: {self.balance}")

account1 = BankAccount("Raul Lopez", 5000)
account2 = BankAccount("Jose Lopez", 3000)

print(account1.holder)
account1.check_balance()
account1.deposit(1000)
account1.withdraw(2000)
account1.check_balance()

print(account2.holder)
account2.check_balance()
account2.deposit(500)
account2.withdraw(400)
account2.check_balance()



