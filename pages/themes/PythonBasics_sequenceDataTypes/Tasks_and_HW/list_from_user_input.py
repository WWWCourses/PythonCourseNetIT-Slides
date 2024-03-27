names_count = int(input("How many names are you going to enter? "))
names = []

for i in range(names_count):
    name = input("Enter a name, please: ")
    names.append(name)

print("*" * 30)
print("The names you've entered are:")
for name in names:
    print(name)
