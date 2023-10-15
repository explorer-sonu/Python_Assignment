# n = int(input("Enter a number:"))
# sum = 0
# while(n>0):
#     sum = sum+n
#     n = n-1
# print("The sum of first n natural number is",sum)

#---------- using for loop -----------#

n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    print(i)  # for checking ke liye
    sum = sum+i
print("The sum of first n natural number is",sum)
print()