A = float(input("ENter your amount"))
B = float(input("ENter your Balance"))
F = 20

if A <= 0:
    print("Amount must be positive")

elif A % 100 != 0:
    print("Amount must be a multiple of 100")

elif A > 20000:
    print("Amount exceeds limit")

elif B >= A+F:
    print("Withdrawing")
else:
    print(" Insufficient balance for fee")