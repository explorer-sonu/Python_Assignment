s1 = input("Enter first string:")
s2 = input("Enter Second string:")
match(s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical string")
    case (s1,s2) if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {}".format(s2,s1))
print()
