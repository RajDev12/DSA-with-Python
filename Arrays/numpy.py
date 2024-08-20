import numpy as np

arr1 = np.array([[5, 6, 7], [1, 2]])
print(arr1)
# NumPy cannot create a regular, rectangular 2D array from these lists because the sublists do not match in size.
# As a result, NumPy will create an array with dtype=object, which means the array elements are stored as Python objects (in this case, lists).
#o/p=> array([list([5, 6, 7]), list([1, 2])], dtype=object)


arr1 = np.array([[5, 6, 7], [1, 2, 3]])
print(arr1)
#NumPy can create a regular 2D array (matrix) from these lists because they have consistent dimensions.
