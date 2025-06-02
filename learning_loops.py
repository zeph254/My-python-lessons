# # While loops are used to repeat a block of code as long as a condition is true.

# name = input("Enter your name: ")
# while name == "":
#     print("Name cannot be empty. Please try again.")
#     name = input("Enter your name: ")
# print(f"Hello, {name}!")

# age =int(input("Enter your age: ")) 

# while age < 0:
#     print("Age cannot be negative. Please try again.")
#     age = input("Enter your age: ")

# print(f"You are {age} years old.")  


# food = input("Enter your favorite food(enter 'quit' to stop): ")
# while food.lower() != "quit":
#     print(f"Your favorite food is {food}.")
#     food = input("Enter your favorite food(enter 'quit' to stop): ")

# pthon compound interest calculator
# principal = 0

# while principal <= 0:
#     principal = float(input("Enter the principal amount: "))
# if principal <= 0:
#     print("Principal amount must be greater than zero. Please try again.")
#     principal = float(input("Enter the principal amount: "))


# rate = 0
# while rate <= 0:
#     rate = float(input("Enter the rate of interest (in %): "))
# if rate <= 0:
#     print("Rate of interest must be greater than zero. Please try again.")
#     rate = float(input("Enter the rate of interest (in %): "))


# time = 0
# while time <= 0:
#     time = int(input("Enter the time (in years): "))
# if time <= 0:
#     print("Time must be greater than zero. Please try again.")
#     time = int(input("Enter the time (in years): "))

# compound_interest = principal * (1 + (rate / 100)) ** time

# print(f"The compound interest is: {compound_interest}")


#  for loops are used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.
for i in range(5):
    print(i)

for x in reversed(range(5)):
    print(x)    

print("happy birthday to you")    

for y in range(1, 6 ,3):
    print(f"Happy birthday to you, {y} times!")