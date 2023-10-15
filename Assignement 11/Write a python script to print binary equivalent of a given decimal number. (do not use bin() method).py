d = 0 
bn = 0
a = 1
n = int(input("Enter a number:"))
while n>0:
    d=n%2
    bn=bn+d*a
    a=a*10
    n=int(n/2)
print("binary number is:",bn)

