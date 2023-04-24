class A():
  def __init__(self, val):
    self.val = val

  def __add__(self,other):
    return self.val + other.val


a = A(1)
b = A(2)

res = 2+3
res2 = a+b

print( res )
print( res2 )
