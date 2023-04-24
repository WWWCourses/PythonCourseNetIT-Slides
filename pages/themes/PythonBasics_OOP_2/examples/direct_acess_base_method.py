class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  """docstring for Employee"""
  def __init__(self, name, age, salary):
    Person.__init__(self,name,age)
    self.salary = salary


pesho = Employee("Pesho",25, 3500)
print(pesho)

