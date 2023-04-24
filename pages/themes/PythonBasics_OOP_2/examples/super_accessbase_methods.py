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
    super().__init__(name,age)
    self.salary = salary

  def __str__(self):
    # return super().__str__() + ". Has salary: {}".format(self.salary)
    return Person.__str__(self) + ". Has salary: {}".format(self.salary)


pesho = Employee("Pesho",25, 3500)
print(pesho)

