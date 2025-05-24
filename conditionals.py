# If statements - conditional statements that execute a block of code if a certain condition is met
# If else statements - conditional statements that execute a block of code if a certain condition is met, or another block of code if the condition is not met


age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")

else:
    print("You are a minor.")

responce = input("Do you want to continue? (yes/no): ")
if responce.lower() == "yes":
    print("Continuing...")
else:
    print("Exiting...")  

online = False
if online:
    print("You are online.")
else:
    print("You are offline.")    
