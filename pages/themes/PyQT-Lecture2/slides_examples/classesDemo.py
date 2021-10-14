class Person:
	def __init__(self, *args):
		print('Person constructor called!')
		print(*args)
		# self.name = args[0]
		# self.age = args[1]

	def greet(self):
		print(f'Hello, {self.name}')

class Citizen:
	def __init__(self, *args):
		print(f'Citizen constructor called!')
		print(*args)

class Student(Person, Citizen):
	def __init__(self, *args):
		print('Student constructor called')
		name,age = args[0:2]
		town = args[2]
		# super().__init__(name,age)
		# super(Student, self).__init__(name, age)


		# super(Student,self).__init__(*args)
		# super(Person,self).__init__(*args)

		Person.__init__(self, name, age)
		Citizen.__init__(self, town)
		# super(Citizen, self).__init__(town)


pesho = Student('Petar', 23, 'Sofia')
# pesho.greet()
