year = int(input("Enter your year :"))
if year%400 == 0 or year%100 != 0 and year%4 ==0:
    print("Leap year")
else:
    print("Not leap year")
print()