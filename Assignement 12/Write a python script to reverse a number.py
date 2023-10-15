n = int(input("Enter a number:"))

# Initiate value to null
revs_number = 0

while (n > 0):
    remainder = n % 10
    revs_number = (revs_number*10) + remainder
    n = n//10
print("The reverse number is:",revs_number)
   








