class Person():
  count = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age

    # increment objects counter:
    Person.count += 1

    # should be __count, but good to show that Person.count != self.count
    self.count = Person.count


  def __str__(self):
    return "{}. {}: {}".format(self.count, self.name, self.age)


maria = Person("Maria", 20)
pesho = Person("Pesho", 30)

print(maria)
print(pesho)