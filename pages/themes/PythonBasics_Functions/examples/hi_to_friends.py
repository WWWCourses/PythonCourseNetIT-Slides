friends = ["Maria", "Ivan", "Alex", "Pesho", ""]

def congrats(lst):
	for item in lst:
		print("Hi {}, nice to see you!".format(item))

congrats(friends)