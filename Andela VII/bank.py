class BankAccount(object):
  def __init__(self, balance):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
    else:
      return "invalid transaction"

my_account = BankAccount(90)
my_account.deposit(90)
my_account.withdraw(40)
my_account.withdraw(1000)

class MinimumBalanceAccount(BankAccount):
  def __init__(self, minimum):
    self.minimum = minimum
    
   