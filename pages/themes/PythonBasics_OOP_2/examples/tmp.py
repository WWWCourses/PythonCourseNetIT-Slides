class Person():
  @staticmethod
  def validate_age():
    if not 0 < age < 100:
      raise ValueError("Invalid age value")

  def __init__(self, name, age):
    self.name = name
    self.age = age

    self.increment_counter()
    # attach count to an object
    self.count = Person.count


  def __str__(self):
    return "{}. {}: {}".format(self.count, self.name, self.age)


maria = Person("Maria", 20)
pesho = Person("Pesho", 30)

print(maria)
print(pesho)

# obviously, we would not want that. So, be careful with class methods!
maria.increment_counter()
pesho.increment_counter()
