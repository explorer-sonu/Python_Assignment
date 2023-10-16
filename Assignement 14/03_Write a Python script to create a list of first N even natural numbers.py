n = int(input("Enter the number you want to print:"))
even_number_list = []
for i in range(1, n+1):
    even_number_list.append(i*2)

print(even_number_list)


#+++++++++++++++++ Second Approch ++++++++++++++++++

# Replace 'N' with the desired number of odd natural numbers you want in the list
N = 10  # Change this to the desired value

current_number = 2
even_numbers_list = []

while len(even_numbers_list) < N:
    even_numbers_list.append(current_number)
    current_number += 2

print(even_numbers_list)
