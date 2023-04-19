class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return "{} = {}".format(self.name, self.age)

	def greet(self):
		print("Hi there! I'm {}, {} years old!".format(self.name, self.age))

maria = Person("Maria Popova", 25)
pesho = Person("Pesho", 27)

print(maria)

# name = Maria Popova
# age = 25