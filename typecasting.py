# Typecasting in Python
# Typecasting is the process of converting a variable from one type to another.
# We can use int(), float(), str(), bool() etc.

# Example:
# Converting a string to an integer
x = int("3")   # x will be 3
print(x)       # Output: 3

name = "dave"
age = 30
email = "7M8yP@example.com"
is_married = True


print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(email)) # Output: <class 'str'>
print(type(is_married)) # Output: <class 'bool'>

# Converting a string to a float
y = float("3.14")  # y will be 3.14
print(y)           # Output: 3.14

# Converting a float to an integer
z = int(3.14)     # z will be 3
print(z)           # Output: 3


# Converting an integer to a string
a = str(3)       # a will be "3"
print(a)         # Output: "3"


# Converting a boolean to a string
b = str(True)    # b will be "True"
print(b)         # Output: "True"


# Converting a string to a boolean
c = bool("True")  # c will be True
print(c)          # Output: True

# Converting a string to a boolean
d = bool("")     # d will be False
print(d)          # Output: False

# Converting a boolean to an integer
e = int(True)    # e will be 1
print(e)          # Output: 1
