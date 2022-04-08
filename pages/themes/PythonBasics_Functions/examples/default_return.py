def foo():
	print("foo() was executed!")

def bar():
	print("bar() was executed!")
	return

print( foo() )
print( bar() )