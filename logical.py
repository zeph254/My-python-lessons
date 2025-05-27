# logical operaters - evaluate multiple conditions
# or - if any condition is true
# and - if all conditions are true
# not - reverse the result


temp = 19

if temp > 30 or temp < 20:
    print("It's warm")
else:
    print("It's not warm")


if temp > 30 and temp < 20:
    print("It's warm")
else:
    print("It's not warm")

if not temp > 30:
    print("It's not warm")    

money = 100
if money > 50 and temp < 20:
    print("You can buy a jacket")
else:
    print("You can't buy a jacket")