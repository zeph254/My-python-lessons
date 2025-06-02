# indexing - accesing elements in a data structure
# indexing in a list
# indexing in a string
# indexing in a tuple


credit_card = "1234-5678-9012-3456"
# indexing in a string
print(credit_card[0])
print(credit_card[1:5])  # Slicing from index 1 to 4
print(credit_card[-1])  # Last character
print(credit_card[::2])  # Last 5 characters

# to reverse a string 
print(credit_card[::-1])

# Format specifiers = {value:flags}format a value based n what flags are inserted

monry1 = 1000
monry2 = 2000

print(f"Money 1: {monry1:,.2f}")  # Format with commas and two decimal places
print(f"Money 2: {monry2:,.2f}")
print(f"Total: {(monry1 + monry2):,.2f}")

  # Format with commas and two decimal places


print(f"Money2 is {monry2:>,.2f} and Money1 is {monry1:,.2f}. The total is {(monry1 + monry2):,.2f}.")  