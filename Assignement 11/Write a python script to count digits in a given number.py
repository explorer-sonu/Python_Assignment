n = int(input("Enter a numbe:"))
count = 0
while n != 0:
    n = n//10
    count += 1
print("Numbers of digit is",count)