s = input("Enter a string:")
s.strip()
match s:
    case s if ' ' in s:
        print("Multiword String")
    case s if ' ' not in s:
        print("Single word string")
print()