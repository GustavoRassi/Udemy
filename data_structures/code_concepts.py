# Fundamental data types

# int:
# float
# bool
# str
# list
# tuple
# set
# dict

print(type(1))
print(type(2 * 4))
print(type(2 / 4))
print(type(2 - 4))

print(2 ** 3) # 2 to the power of 3 ()
print(5 // 4) # prints integer of result (0.80 = 0)
print(6 % 4) # prints how many times 4 fits in 6 (which is once = 4)

# math functions
print(round(3.1)) # prints closest integer (3)
print(abs(-20)) # absolute value of of -20 is 20

# operator precedence
print((20 - 3) + 2 ** 2)

# ()
# **
# * /
# + -

# binary conversion: convert any binary into an int value
print(bin(5)) # prints binary number of 5
x = bin(5)
print(int(x, 2)) # print the int value of binary number x

# variables
user_iq = 190
print(user_iq)

# dunder variables
# __variableX__ : double underscore

# this is valid: assigns value to variables the same order is declared
x, y, z = 1, 2, 3 # x=1, y=2, z=3
print(x, y, z)

# augmented assignment operator: assign value with the sum of itself
some_value = 5
some_value = some_value + 2
# or: some_value += 2 (it's the same thing)

# strings
# str = sequence or order of characters stored in memory
x = 100
print(type(x)) # prints data type of variable
x = str(x) # converts int to str
print(type(x))
# escape sequence
weather = 'it\'s sunny'
print(weather)

# built-in functions
print("Hello".find("o"))
print("Hello".upper())
greet = "Gustavo Rassi"
print(greet.replace('Gu', 'Ra'))
print(greet)

# booleans
print(bool(1)) # prints True because 1 = true
print(bool(0))
print(bool('Gustavo')) # prints True

# ⁡⁣⁢⁣Lists⁡
li = [1,2,3,4,5]
# list slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
# NOTE: character assignments are immutable.
# unlike lists, lists are not, so you can change elements.
greet = 'hello'
#greet[0] = 'H' # this will give an error
amazon_cart[0] = 'laptop' # this won't give you an error
print()
new_cart = amazon_cart[0:3] # copies list to new list from index 0 to index 2 (3 not included).

# matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
matrix[0][1] = 0
print(matrix)

# list methods
basket = ['a','b','c','d','e']
new_list = basket.append('k')
print(new_list) # prints None because the list is empty
print(basket) # prints the list including 100 at the end
basket.extend(['f','g','h','j','m'])
print(basket)
basket.pop() # removes the last element
removed_element = basket.pop(4) # removes element at index 4 and returns it
print(basket)
basket.remove('g') # removes elements 

list1 = ['a','b','d','c','e']
print(f"Unsorted list: {list1}")
list1.sort()
print(f"Sorted list: {list1}")

# ⁡⁢⁢⁡⁣⁣⁢⁡⁣⁢⁣WAYS OF REVERSING A LIST⁡⁡⁡

# Original list of numbers.
my_list = [1,2,3,4,5]

# Method 1: Using list.reverse()
# This method reverses the original list.
my_list.reverse()
print(f"Reversed list: {my_list}") # Output: [5,4,3,2,1]

# Method 2: Using list[::-1]
# This method uses slicing technique to create a copy of the reversed list, while the original list is unchanged
# Reset the original list
my_list = [1,2,3,4,5]
new_list = my_list[::-1]
print(f"Copy of reversed list: {new_list}") # Output: [5,4,3,2,1]
print(f"Original list: {my_list}") # Output: [1,2,3,4,5]
a,b,c = 1,2,3
print(a,b,c) # Output: 1, 2, 3

# list unpacking: a way of unpacking a list from its elements
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a,b,c,other,d)

# ⁡⁣⁢⁣Data Structure: Dictionary⁡
# an unordered key-value pair
# a way to organize data with different pros and cons.
# Example: dictionaries are good for storing information of a user
user = {
    'first_name': "Gustavo",
    'last_name': "Rassi",
    'email': "grassi.code@gmail.com",
    'age': 23
}
if user.get('age') is None:
    print(f"{user['first_name']} {user['last_name']}\'s age is not registered.")
else:
    print(f"{user['first_name']} {user['last_name']} is {user['age']} years old.")

print(user.items()) # Prints the whole dictionary
user.update({'age': 30}) # updates the key to the new value
print(user['age'])
print(user.get('age', 55)) # if 'age' doesn't exist, it prints 55 (error handling)

print('e' in user['last_name']) # Output: True

print('Rassi' in user.values())

user2 = user.copy() # Copies user information to new user

# Data Structure: Tuples
# Tuples are used for coordinates
# For example, consider Uber service where the uber needs your coordinates to locate you.
my_tuple = (1,2,3,4,5)

# Methods
print(my_tuple.index(2)) # Returns index of value
print(my_tuple.count(4)) # Returns number of occurrences of the value

# ⁡⁣⁢⁣Data Structure: Set⁡
# Definition: Unordered collection of unique items.
my_set = {1,2,2,3,4,5,5}
print(f"Created Set: {my_set}") # Output: {1, 2, 3, 4, 5}
# Since sets have unique items, the output is the unique items (no duplicates).
item = None
print(item)

# Ternary operator
# condition_if_true if condition else condition_if_else
is_friends = False
thismessage = "this is allowed" if is_friends else "message not allowed"
print(thismessage)