import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(my_array.shape)
my_new_array = np.zeros(5)
print(my_new_array)
my_random_array = np.random.random((5))
print(my_random_array)
my_2d_array = np.zeros((2, 3))
print(my_2d_array)
my_array = np.array([[1, 2], [3, 4]])
print(my_array[0][1])
print(my_array.shape)
my_array_column_2 = my_array[:, 1]
print(my_array_column_2)
