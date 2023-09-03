print("Enter three number")
a,b,c=int(input()),int(input()),int(input())
print((a if a>c else c)if a>b else(b if b>c else c))