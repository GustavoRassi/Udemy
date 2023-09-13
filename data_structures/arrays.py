import numpy as np

my_array = np.array([1,2,3,4,5])
print(f"My array: {my_array}") # Output: [1 2 3 4 5]

# Adding element 2 at the end
my_array = np.append(my_array, 2)
print(f"Array after element appended: {my_array}") # Output: [1 2 3 4 5 2]

# Removing an element at a specific index
my_array = np.delete(my_array, 1)
print(f"Array after deleted element: {my_array}") # Output: [1 3 4 5 2]

