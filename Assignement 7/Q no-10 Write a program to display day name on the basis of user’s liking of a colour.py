s1 = input("What is your favourite colour:")
l1 = ["yellow","blue","orange","White","Black","red"]
for colour in l1:
    if colour in s1:
        c = colour
        break
    else:
        c="other"
        match c:
            case "yellow":
                print("Monday")
            case "blue":
                print("Tuesday")
            case "orange":
                print("Wednesday")
            case "White":
                print("Thursday")
            case "Black":
                print("Friday")
            case "red":
                print("Saturday")
            case "other":
                print("Sunday")
print()