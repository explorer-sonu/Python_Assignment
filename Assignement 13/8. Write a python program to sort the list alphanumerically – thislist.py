thislist  = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

#++++++++++ secons Approch +++++++++++++++++

thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

# Sort the list alphanumerically without using a custom key function
sorted_list = sorted(thislist, key=lambda x: (x.isdigit(), x.lower()))

# Print the sorted list
for item in sorted_list:
    print(item)
