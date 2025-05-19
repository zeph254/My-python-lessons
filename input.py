# input() = A function that reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# # The trailing newline is removed from the string. If the input function is called, the program will wait for the user to enter a value.
# # The input function returns the value entered by the user as a string.

# name = input("Enter your name: ")
# print("Hello " + name)

name = input("What is your name ?: ")
age = input("What is your age ?: ")  # || int(input("What is your age ?: "))  # This will raise an error if the input is not a number
# age = input("What is your age ?: ")  # This will raise an error if the input is not a number
age = int(age)  # Convert age to an integer
age = age + 1  # Increment age by 1
# age = str(age)  # Convert age back to a string if needed
email = input("What is your email ?: ")


print(f"Hello {name}!")
print(f"You are {age} years old!")
print(f"Your email is {email}!")


item = input("WHAT ITEM WOULD YOU LIKE TO BUY?: ")
price = float(input("WHAT IS THE PRICE OF THE ITEM?: "))
quantity = int(input("HOW MANY ITEMS WOULD YOU LIKE TO BUY?: "))
total = price * quantity
print(f"You have bought {quantity} {item}(s) for a total of ${total}")
