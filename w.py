class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
    else:
      print("invalid transaction")

my_account = BankAccount(90)
my_account.balance(90)
my_account.deposit(40)
my_account.withdraw(1000)

class MinimumBalanceAccount(BankAccount):
  def __init__(self):
      BankAccount.__init__(self)
   