print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("Enter your Choice")
choice = int(input())
match choice:
    case 1:
        print("Enter Two numbers:")
        a,b=int(input()),int(input())
        c = a+b
        print("Sum is ",c)
    case 2:
        print("Enter Two numbers:")
        a,b=int(input()),int(input())
        c = a-b
        print("Difference is ",c)
    case 3:
        print("Enter Two numbers:")
        a,b=int(input()),int(input())
        c = a*b
        print("Product is ",c)
    case 4:
        print("Enter Two numbers:")
        a,b=int(input()),int(input())
        c = a/b
        print("Division is ",c)
    case _:
        print("Invalid choice")
        