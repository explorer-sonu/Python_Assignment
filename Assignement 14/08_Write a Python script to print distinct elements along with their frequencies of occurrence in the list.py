# Replace the 'my_list' with your list of elements
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5]

# Initialize an empty dictionary to store element frequencies
element_frequencies = {}

# Count the frequency of each element in the list
for element in my_list:
    if element in element_frequencies:
        element_frequencies[element] += 1
    else:
        element_frequencies[element] = 1

# Print distinct elements with their frequencies
for element, frequency in element_frequencies.items():
    print(f"Element {element} occurs {frequency} time(s) in the list.")