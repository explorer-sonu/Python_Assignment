n = int(input("Enter the number you want to print:"))
natural_number_list = []
for i in range(1, n+1):
    natural_number_list.append(i)

print(natural_number_list)

#+++++++++++++++++++ second approch ++++++++++++++++++

# Replace 'N' with the desired number of first natural numbers you want in the list
N = 10  # Change this to the desired value

natural_numbers_list = []
current_number = 1

while len(natural_numbers_list) < N:
    natural_numbers_list.append(current_number)
    current_number += 1

print(natural_numbers_list)