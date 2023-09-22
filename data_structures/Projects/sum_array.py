# Sum Array
# The sum of the items in the array and print the result.
import numpy as np

my_array = np.array([1,2,4,5]) # Create array with numpy
array_sum = sum(my_array) # Sum of the elements of the array 
print(f"Array: {my_array}") # Output: [1 2 4 5]
print(f"Sum array = {array_sum}") # Output: Sum array = 12

my_tuple = (1,2,3,4,5)
print(f"My tuple: {my_tuple}") # Output: (1, 2, 3, 4, 5)
my_dictionary = { # dictionary creation
    'name': "Gustavo",
    'email': "grassi.code",
    'age': 23
}

print(f"\nMy dictionary: {my_dictionary}") # Output: My dictionary: {'name': 'Gustavo', 'email': 'grassi.code', 'age': 23}

print('user' in my_dictionary) # prints true
my_array2 = np.array(range(0,50)) # creates array of elements from 0 to 49
print(my_array2) # Output: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
print("Udemy!")