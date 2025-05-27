# name = input("Enter your name: ")

# # result = len(name)
# result = name.find('a')
# result = name.count('a')
# result = name.upper()
# result = name.lower()
# result = name.title()
# result = name.strip()
# result = name.replace('a', 'o')
# result = name.isalpha()
# result = len(name)
# result = name.startswith('A')
# result = name.endswith('a')
# result  = name.isdigit()
# # result = name.isalnum()
# # result = name.islower()
# # result = name.isupper()
# # result = name.isspace()



# print(f"Your name has {result} characters.")


username = input("Enter your username: ")

if len(username) > 12:
    print("Username must be **less than or equal to** 12 characters.")
elif len(username) < 3:
    print("Username must be at least 3 characters.")
elif " " in username:  # ✅ This is the correct check for spaces
    print("Username must not contain spaces.")
elif username == "":
    print("Username must not be empty.")
elif any(char.isdigit() for char in username):
    print("Username should not contain digits.")
else:
    print("Welcome, " + username + "! Your username is valid.")
