a = int(input("Enter a number: "))

if a < 0:
    print("Negative")
elif a <= 10:
    print("Small")
elif a <= 100:
    print("Medium")
else:
    print("Large")