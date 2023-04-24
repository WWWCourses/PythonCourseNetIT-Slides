class A():
  @staticmethod
  def staticMethod():
    print("STATIC method fired!")
    print("Nothing is bound to me")
    print("~"*30)

  @classmethod
  def classMethod(cls):
    print("CLASS method fired!")
    print(str(cls)+" is bound to me")
    print("~"*30)

  # normal method
  def normalMethod(self):
    print("'normalMethod' fired!")
    print(str(self)+" is bound to me")
    print("~"*30)


  def __init__(self, val):
    self.val = val

a = A(1)
a.staticMethod()
a.classMethod()
a.normalMethod()