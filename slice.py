# slicing = cretae a substring by extracting a portion of the string

name = "Bro dave"

first_name  = name[0:3]
print(first_name)  # Output: B

last_name = name[4:8]
print(last_name)  # Output: dave


funky_name = name[0:8:2]
# funky_name = name[::2]  # This will give the same result
print(funky_name)  # Output: Bro dave


reversed_name = name[::-1]
print(reversed_name)  # Output: evad orB daveB


#slice
website = "http://google.com"

slice = slice(7, -4)
print(website[slice])  # Output: google

