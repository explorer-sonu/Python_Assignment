thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# Iterate through the list and replace "SQL" with "NoSQL" and "Reactnative" with "Flutter"
for i in range(len(thislist)):
    if thislist[i] == "SQL":
        thislist[i] = "NoSQL"
    elif thislist[i] == "Reactnative":
        thislist[i] = "Flutter"

# Print the modified list
print(thislist)
