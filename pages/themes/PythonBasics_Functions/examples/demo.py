def logger_dec(f):
  def tmp():
    print("FOO is logged!")
    f()
  return tmp

@logger_dec
def foo():
  print("I'm FOO")

foo()




