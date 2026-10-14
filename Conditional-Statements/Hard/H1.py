S = float(input("Enter your score: "))

if S < 0 or S > 100:
    print("Invalid score")
elif S >= 90:
    print("A")
elif S >= 80:
    print("B")
elif S >= 70:
    print("C")
elif S >= 60:
    print("D")
else:
    print("F")
    