
# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a function (create_numpy_array) that takes a list of numbers and returns a NumPy array.
"""

### YOUR CODE HERE:

### TEST:
print(create_numpy_array([1, 2, 3, 4, 5]))

### EXPECTED OUTPUT:
# [1 2 3 4 5]


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function (array_sum) that takes a NumPy array and returns the sum of its elements.
"""

### YOUR CODE HERE:

### TEST:
print(array_sum(np.array([1, 2, 3, 4, 5])))

### EXPECTED OUTPUT:
# 15


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a function (evens_in_array) that takes a NumPy array and returns a new array containing only the even numbers.
"""

### YOUR CODE HERE:

### TEST:
print(evens_in_array(np.array([1, 2, 3, 4, 5, 6])))

### EXPECTED OUTPUT:
# [2 4 6]


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function (count_greater_than) that takes a NumPy array and a threshold value, and returns the count of elements greater than the threshold.
"""

### YOUR CODE HERE:

### TEST:
print(count_greater_than(np.array([1, 2, 3, 4, 5]), 3))

### EXPECTED OUTPUT:
# 2


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a function (access_element) that takes a NumPy array and an index, and returns the element at that index.
"""

### YOUR CODE HERE:

### TEST:
print(access_element(np.array([10, 20, 30, 40, 50]), 3))

### EXPECTED OUTPUT:
# 40


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Create a function (slice_array) that takes a NumPy array and two indices, start and end, and returns the sliced array.
"""

### YOUR CODE HERE:

### TEST:
print(slice_array(np.array([10, 20, 30, 40, 50]), 1, 4))

### EXPECTED OUTPUT:
# [20 30 40]
