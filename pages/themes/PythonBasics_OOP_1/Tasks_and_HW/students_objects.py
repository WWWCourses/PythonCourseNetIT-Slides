class Student:
	def __init__(self, name, subjects):
		self.name = name
		self.subjects = subjects

	def greet(self):
		print("Hello, I'm {}. My favourite subjects are: ".format(self.name))
		for item in self.subjects:
			print("\t{}".format(item))


# objects creation:
ivan = Student("Ivan Ivanov", ["maths", "phisics"])
alex = Student("Alex Petrov", ["arts", "music"])
maria = Student("Maria Popova", ["chemistry", "biology"])

# use objects:
ivan.greet()
alex.greet()
maria.greet()