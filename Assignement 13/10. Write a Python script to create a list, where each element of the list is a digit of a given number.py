# Get the number from the user as a string
number_str = input("Enter a number: ")

# Initialize an empty list to store the individual digits
digit_list = []

# Iterate through each character in the number string
for char in number_str:
    if char.isdigit():
        digit_list.append(int(char))  # Convert the character to an integer and add it to the list

# Print the list of digits
print("List of digits:")
print(digit_list)