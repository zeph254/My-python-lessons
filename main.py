print('hello World!')
# print('hello World!')

# variables
name = 'dave'
age = 30    
email = "7M8yP@example.com"

print(name)
print(age)

print(f"Hello {name} you are {age} years old and your email is {email}")

# intergers
age = 30
# floats
height = 1.75
# strings
name = "dave"
# booleans
is_married = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_married))

print(f"Hello {name} you are {age} years old and your email is {email} and your height is {height} and you are married {is_married}")


# string concatenation
first_name = "dave"
last_name = "smith"
full_name = first_name + " " + last_name
print(full_name)

# string formatting
age = 30
print(f"Hello {name} you are {age} years old and your email is {email} and your height is {height} and you are married {is_married}")

# string methods
name = "dave"
print(name.upper())
print(name.lower())
print(name.title())

is_married = True
if is_married:
    print("You are married")
else:
    print("You are not married")

# string slicing
name = "dave"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# string length
name = "dave"
print(len(name))