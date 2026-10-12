subtotal = float(input("Enter subtotal: "))

if subtotal < 0:
    print("Invalid subtotal")
elif subtotal >= 5000:
    discount = subtotal * 20 / 100
    total = subtotal - discount
    print("Discount:", discount)
    print("Final Amount:", total)
elif subtotal >= 2500:
    discount = subtotal * 10 / 100
    total = subtotal - discount
    print("Discount:", discount)
    print("Final Amount:", total)
else:
    discount = 0
    total = subtotal
    print("Discount:", discount)
    print("Final Amount:", total)