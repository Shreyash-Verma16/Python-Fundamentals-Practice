items = ["shirt", "charger", "bottle"]
a = str(input("Enter your destination : "))
b = "jacket"
c = "sunscreen"

if a == "Cold":
    if a in items:
        print(items.insert(2,"Jacker"))
    else:
        print(items)
if a == "hot":
    if c in items:
        print(items.append("sunscreen"))
    else:
        print(items)
