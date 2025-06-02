# While loops are used to repeat a block of code as long as a condition is true.

name = input("Enter your name: ")
while name == "":
    print("Name cannot be empty. Please try again.")
    name = input("Enter your name: ")
print(f"Hello, {name}!")

age =int(input("Enter your age: ")) 

while age < 0:
    print("Age cannot be negative. Please try again.")
    age = input("Enter your age: ")

print(f"You are {age} years old.")  


food = input("Enter your favorite food(enter 'quit' to stop): ")
while food.lower() != "quit":
    print(f"Your favorite food is {food}.")
    food = input("Enter your favorite food(enter 'quit' to stop): ")