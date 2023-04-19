class Person:
	def __init__(self, name, age):
		self.name = name
		self.__age = age

	def __str__(self):
		return """
			name = {}
			__age = {}
		""".format(self.name, self.__age)
	def greet(self):
		print("Hi there! I'm {}, {} years old!".format(self.name, self.age))

maria = Person("Maria Popova", 25)
maria.__age = 100

print(maria.__age)
print(maria)

print( maria.__dir__())
# name = Maria Popova
# age = 25