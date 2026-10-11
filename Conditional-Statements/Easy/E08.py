day = int(input("Enter day number (1-7): "))

if day >= 1 and day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day")

#used ai in this question (Copilot)