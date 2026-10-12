a = int(input("Enter your number between 1 to 12: "))

if a <= 0 or a >= 13:
    print("Invalid number")
else:
    if a <= 3:
        print("Q1")
    elif a <= 6:
        print("Q2")
    elif a <= 9:
        print("Q3")
    elif a <=12:
        print("Q4")
     