month =int(input("Enter month name:")) 
if month in (1,3,5,7,8,10,12):
   print("31 Days")
if month in (4,6,9,11):
   print("30 Days")
if month ==2:
   print("28 or 29 Days")
else:
   print("Invalid month name")