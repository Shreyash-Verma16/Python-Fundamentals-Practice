items = ["shirt", "charger", "bottle"]

a = input("Enter your destination: ")

if a.lower() == "cold":
    if "jacket" not in items:
        items.insert(1, "jacket")

elif a.lower() == "hot":
    if "sunscreen" not in items:
        items.append("sunscreen")

print(items)
