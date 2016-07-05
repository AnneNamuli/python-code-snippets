class BankAccount():

    """docstring for BankAccount"""
def __init__(self, balance):
	self.balance = balance

"""docstring for method """
def deposit(self, amount):
	self.__checkinput(amount)
	#update self.balance below
	

"""docstring for method """
def withdraw(self, amount):
	self.__checkinput(amount)
	if(amount > self.balance):
		raise Exception("invalid transaction")
	#update self.balance below

"""docstring for method """	
def __repr__(self):
	#how to represent every instance
	#implement it
	pass

"private method to validate input"
def __checkinput(self, value):
	if value < 0:
		return ("Enter a valid amount")
class MinimumBalanceAccount(BankAccount):
	"""docstring for ClassName"""
	def __init__(self,arg):
		#implement

mine = BankAccount(200)
print (mine.balance) #200

mine.deposit(400)
print (mine.balance) #600

mine.withdraw(500)
print (mine.balance) #100

mine.withdraw(200)
print (mine.balance) #Exception
if __name__ == '__main__':
	unittest.main()