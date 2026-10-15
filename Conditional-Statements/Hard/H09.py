O = float(input("Enter your order price")) 
Z = input("Enter zone (local/extended")
F = input("Fragile item? (yes/no")

if O < 0:
    print("Invalid")
elif Z != "local" and Z != "extended":
    print("Invalid")
else:
    if O >= 1500:
        delivery_charge = 0
    elif Z == "local":
        delivery_charge = 30
    else:
        delivery_charge = 70

    if F == "yes":
        delivery_charge += 25
        print("INR", delivery_charge)