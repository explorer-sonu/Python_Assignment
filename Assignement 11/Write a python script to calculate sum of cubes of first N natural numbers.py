n = int(input("Enter a number:"))
sum = 0
while(n > 0):
    print(n*n*n) # for checking ke liye
    sum = sum + n*n*n
    n = n-1
print("The sum the first cubes of n natural number is ",sum)
print(sum)
print()

#---------------- using for loop ------------------#
# n = int(input("Enter a number:"))
# sum = 0
# for i in range(1,n+1):
# print(i*i*i)  #  for checking ke liye
#     sum = sum + i*i*i
# print(sum)