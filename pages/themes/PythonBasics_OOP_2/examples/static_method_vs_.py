class A():
  @staticmethod
  def staticMethod():
    print("STATIC method fired!")

  @classmethod
  def classMethod():
    print("CLASS method fired!")

  # we can not define a "normal" function inside class
  def foo():
    print("FOO fired!")

  def __init__(self, val):
    self.val = val

class B(A):
  def __init__(self, name):
    self.name = name


a = A(1)
b = B("test")

a.staticMethod()
b.staticMethod()
a.foo()
# b.classmethod()