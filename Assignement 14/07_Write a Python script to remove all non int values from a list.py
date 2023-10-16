# Replace the 'my_list' with your list of mixed values
my_list = [10, 'apple', 5.5, 20, 'banana', 15, 30, 'cherry']

# Use a list comprehension to filter out non-integer values
filtered_list = [x for x in my_list if isinstance(x, int)]

print("List with non-integer values removed:", filtered_list)

