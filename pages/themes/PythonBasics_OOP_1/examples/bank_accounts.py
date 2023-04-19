class BankAccount(object):
	"""Represent a simplified bank account

	Attributes:
	    balance (float): current balance
	    owner (string): owner name
	"""

	def __init__(self, owner_name, initial_balance, currency):
		self.owner = owner_name
		self.__balance = initial_balance
		self.currency = currency

	def deposit(self, amount):
		self.__balance += amount

	def withdraw(self, amount):
		if amount > self.__balance:
			print("Not enough funds!")
			return False
		else:
			self.__balance -= amount

	def report(self):
		print("{} has {}{}".format(self.owner, self.__balance, self.currency))


maria_account = BankAccount("Maria", 0, "lv")
pesho_account = BankAccount("Pesho", 0, "$")

maria_account.deposit(100)
# change "hidden"  field:
maria_account._BankAccount__balance = 1_000_000
maria_account.report()

