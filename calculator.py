operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operator."

print("Result:", result)


unit = input("Enter the unit (C/F): ").upper()
temperature = float(input("Enter the temperature: "))

if unit == "C":
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temp}°F")
elif unit == "F":
    converted_temp = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temp}°C")
else:
    print("Error! Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")