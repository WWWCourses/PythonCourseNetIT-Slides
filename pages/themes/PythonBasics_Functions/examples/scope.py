if 0:
  x = 10

  def f1():
    # creates new local variable x
    x = 99
    print("x = {} inside f1()".format(x))

  f1()
  print("x = {} outside f1()".format(x))

# passing list to function
if 0:
  l = [1,2]

  def foo(lst):
    lst.append(3)

  def bar(lst):
    lst = [4,5]

  foo(l)
  print(l)
  bar(l)
  print(l)

if 1:
  x = 5

  def foo(y):
    y = 1

  foo(x)
  print(x)

  a = 5
  b = a
