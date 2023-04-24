class Person():
  count = 0

  @classmethod
  def increment_counter(cls):
    cls.count += 1
    print("count:",cls.count )

  @staticmethod
  def validate_age(age):
    if not 0 < age < 100:
      raise ValueError("Invalid age value")
    else:
      return True

  def __init__(self, name, age):
    self.name = name
    Person.validate_age(age)
    self.age = age

    self.increment_counter()
    # attach count to an object
    self.count = Person.count


  def __str__(self):
    return "{}. {}: {}".format(self.count, self.name, self.age)


maria = Person("Maria", 20)
pesho = Person("Pesho", 300)

print(maria)
print(pesho)

# obviously, we would not want that. So, be careful with class methods!
maria.increment_counter()
pesho.increment_counter()