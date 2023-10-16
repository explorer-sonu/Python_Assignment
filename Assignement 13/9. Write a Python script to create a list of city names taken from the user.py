# Initialize an empty list to store the city names
city_list = []

# Ask the user for input
while True:
    city_name = input("Enter a city name (or type 'exit' to finish): ")
    
    if city_name.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'
    
    city_list.append(city_name)  # Add the city name to the list

# Print the list of city names
print("List of city names:")
for city in city_list:
    print(city)

#+++++++++++++++++ Second Approch +++++++++++++++++++++

# Initialize an empty list to store the city names
city_list = []

# Ask the user for the number of cities to input
num_cities = int(input("Enter the number of cities you want to add: "))

# Ask the user to input city names
for i in range(num_cities):
    city_name = input(f"Enter city {i + 1}: ")
    city_list.append(city_name)

# Print the list of city names
print("List of city names:")
for city in city_list:
    print(city)