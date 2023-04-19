class BankAccount(object):
	"""Represent a simplified bank account

	Attributes:
	    balance (float): current balance
	    owner (string): owner name
	"""

	def __init__(self, owner_name, initial_balance):
		self.owner = owner_name
		self.balance = initial_balance

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

maria_account = BankAccount("Maria", 1_300)
pesho_account = BankAccount("Pesho", 100)
