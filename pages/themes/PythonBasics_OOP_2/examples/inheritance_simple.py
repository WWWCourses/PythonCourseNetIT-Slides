class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  pass

pesho = Employee("Pesho",25)

print(pesho)

