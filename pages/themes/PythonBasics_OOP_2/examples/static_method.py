class Person():
  @staticmethod
  def validate_age(age):
    if not 0 < age < 100:
      raise ValueError("Invalid age value")

  def __init__(self, name, age):
    self.name = name
    try:
      self.validate_age(age)
    except:
      raise
    else:
      self.age = age

  def __str__(self):
    return "{}: {}".format(self.name, self.age)


maria = Person("Maria", 20)
print(maria)

pesho = Person("Pesho", 300)
print(pesho)