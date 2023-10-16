firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

# Append elements from secondlist to firstlist using extend()
firstlist.extend(secondlist)

# Print the updated firstlist
print(firstlist)

# +++++++++++++++ second approch ++++++++++++++++

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

# Append elements from secondlist to firstlist using the + operator
firstlist += secondlist

# Print the updated firstlist
print(firstlist)

