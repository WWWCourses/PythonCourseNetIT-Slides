class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  def __str__(self):
    return "{} is  employee".format(self.name)

maria = Person("Maria", 20)
pesho = Employee("Pesho",25)

print(maria)
print(pesho)

