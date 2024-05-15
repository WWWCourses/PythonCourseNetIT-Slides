import numpy as np

# create one-dimensional array
arr1d = np.array([1, 2, 3])
# create two-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(f'arr1d: \n{arr1d}\n')
print(f'arr2d: \n{arr2d}\n')

print(f'arr1d.shape: {arr1d.shape}') # (rank 1, axes 0)
print(f'arr2d.shape: {arr2d.shape}') # (rank 2, axes 0 and 1)