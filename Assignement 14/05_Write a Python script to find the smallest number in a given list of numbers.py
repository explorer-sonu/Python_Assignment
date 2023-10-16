# Replace the 'numbers' list with your list of numbers
numbers = [12, 45, 67, 89, 6, 34, 56, 78]

# Initialize the minimum number to the first number in the list
min_number = numbers[0]

# Iterate through the list and update min_number if a smaller number is found
for number in numbers:
    if number < min_number:
        min_number = number

print("The smallest number in the list is:", min_number)