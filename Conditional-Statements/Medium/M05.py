w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))

if w <= 0 or h <= 0:
    print("Weight and height must be positive values.")
else:
    c = w / (h ** 2)

    if c < 18.5:
        print("Underweight")
    elif c < 25:
        print("Normal weight")
    elif c < 30:
        print("Overweight")
    else:
        print("Obese")
