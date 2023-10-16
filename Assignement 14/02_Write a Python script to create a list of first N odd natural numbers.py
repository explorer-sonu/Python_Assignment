n = int(input("Enter the number you want to print:"))
odd_number_list = []
for i in range(1, n+1):
    odd_number_list.append(i*2-1)

print(odd_number_list)

#+++++++++++++++++++ Second Approch +++++++++++++++++

# Replace 'N' with the desired number of odd natural numbers you want in the list
N = 10  # Change this to the desired value

odd_numbers_list = []
current_number = 1

while len(odd_numbers_list) < N:
    odd_numbers_list.append(current_number)
    current_number += 2

print(odd_numbers_list)
