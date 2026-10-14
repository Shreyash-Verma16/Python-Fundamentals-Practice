D = int(input("Enter date"))
M = int(input("Enter Month"))
Y = int(input("Enter Year "))

if M < 1 or M > 12:
    print("Invalid Month")
elif D<1:
    print("Invalid date")

elif M in [1, 3, 5, 7, 8, 10, 12]:
    if D <= 31:
        print("Valid date")
    else:
        print("Invalid date")
elif M in [4, 6, 9, 11]:
    if day <= 30:
        print("Valid date")
    else:
        print("Invalid date")
else:
    if(Y%400 == 0) (Y % 4 == 0 and Y % 100 != 0):
         max_days = 29
    else:
        max_days = 28

    if day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")