# Replace the 'numbers' list with your list of numbers
numbers = [12, 45, 67, 89, 34, 56, 78]

# Initialize the maximum number to the first number in the list
max_number = numbers[0]

# Iterate through the list and update max_number if a larger number is found
for number in numbers:
    if number > max_number:
        max_number = number

print("The greatest number in the list is:", max_number)
