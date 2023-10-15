# n = int(input("Enter a number:"))
# sum = 0
# while(n > 0):
#     print(n*2-1)
#     sum = sum + n*2-1
#     n = n-1
# print("The sum the first n odd natural number:",sum)
# print()

#--------------using for loop --------------#

n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    print(i*2-1)  # for checking ke liye
    sum = sum + i*2-1
print("The sum the first n odd natural number:",sum)
print()
