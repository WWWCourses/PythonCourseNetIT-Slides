# user_name_input = 'ada'
# user_name = user_name_input.capitalize()

# print(user_name_input)
# print(user_name)

# example 1
# name = 'Iva'
# print(f'Hello {name}, nice to see you!')

# # example 2
# x = 2
# y = 4
# print(f'x+y={x+y}')


# x = 5
# y = 10
# formatted = "{0}-{0}-{0}, {1}-{1}".format(x,y)
# print(formatted)


x = 1
y = 3
z = 4

sum_vals = x+y+z
avg = sum_vals/3


# Calculate and displays the sum, average, minimum, and maximum values. Use the str.format() method to format the output as  floating point number with 2 decimal places.

print('Sum = {:.2f}'.format(sum_vals))
print('Average = {:.2f}'.format(avg))
print('Min = {:.2f}'.format(min(x,y,z)))
print('Max = {:.2f}'.format(max(x,y,z)))