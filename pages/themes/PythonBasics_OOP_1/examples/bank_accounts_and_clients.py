class BankAccount(object):
	"""Represent a simplified bank account

	Attributes:
	    balance (float): current balance
	    owner (string): owner name
	"""

	def __init__(self, owner_obj, initial_balance, currency):
		self.owner = owner_obj.get_name()
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

class Client(object):
	"""docstring for Client"""
	def __init__(self, first_name, sur_name, addres):
		self.first_name = first_name
		self.sur_name = sur_name
		self.addres = addres

	def get_name(self):
		return "{} {}".format(self.first_name, self.sur_name)

# make client objects
maria = Client("Maria", "Popova", {
	"town": "Sofia",
	"street": "Nezabravka",
	"number": 14
})

pesho = Client("Pesho", "Ivanov", {
	"town": "Sofia",
	"street": "Nezabravka",
	"number": 99
})


# make maria's account:
maria_account = BankAccount(maria, 0, "lv")
maria_account.deposit(100)
# change "hidden"  field:
maria_account._BankAccount__balance = 1_000_000
maria_account.report()

# make pesho's account:
pesho_account = BankAccount(pesho, 0, "$")
pesho_account.deposit(999)
pesho_account.report()
