I = float(input("Enter income: "))

if I < 0:
    print("Invalid income")
else:
    tax = 0.0

    if I > 1000000:
        tax += (I - 1000000) * 0.20
        I = 1000000

    if I > 500000:
        tax += (I - 500000) * 0.10
        I = 500000

    if I > 250000:
        tax += (I - 250000) * 0.05

    print("INR", tax)