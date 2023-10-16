thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# Iterate through the list and print items along with their index
for index in range(len(thislist)):
    item = thislist[index]
    print(f"Item at index {index} is: {item}") # where f is represent by string value 


# +++++++++++++ Second Approch ++++++++++++++++

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# Iterate through the list and print items along with their index
for index, item in enumerate(thislist):
    print(f"Item at index {index} is: {item}")