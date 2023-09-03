n = int(input("Enter a number:"))
match n:
    case n if n%2 == 0:
        print("Saurabh Shukla")
    case n if n<0 and n%2:
        print("Prateek Jain")
    case n if n>0 and n%2:
        print("Aditya Choudhary")
print()