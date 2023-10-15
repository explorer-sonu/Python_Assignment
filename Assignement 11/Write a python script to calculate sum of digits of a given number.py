n = int(input("Enter a numbe:"))
sum = 0
while n > 0:
    sum = sum + n%10
    n = n//10
print("Numbers of digit is",sum)