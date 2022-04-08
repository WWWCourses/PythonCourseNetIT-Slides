if 0:
  def signup(**kwargs):
    for k,v in kwargs.items():
      print("{} - {}".format(k,v))


  signup(user="ada", age=28)
  signup(user="ada", age=28, town="london")

if 0:
  def point_3d(x,y,z):
    print(x,y,z)

  point={
    "x": 10,
    "y": 5,
    "z": 21
  }
  point_3d(**point)

if 0:
  def menu_print(fruit, price):
    print("{:.<20s}{:.2f}".format(fruit,price))


  menu_print(**{
    "price": 2.5,
    "fruit": "apple"
  })




import inspect

def caller(f):
  f()


def foo():
  print("I'm: ", inspect.stack()[0][3])
  print("caller: ", inspect.stack()[1][3])

def bar():
  print("I'm: ", inspect.stack()[0][3])
  print("caller: ", inspect.stack()[1][3])


caller(foo)
caller(bar)

x = caller
x(bar)