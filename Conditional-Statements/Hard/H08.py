A = int(input("Enter your age: "))
MI = float(input("Enter your income: "))
CS = int(input("Enter your credit score: "))

if A < 18:
    print("Invalid age")

elif CS < 300 or CS > 850:
    print("Invalid score")

elif A >= 21 and A <= 60 and MI >= 30000 and CS >= 700:
    print("Eligible")

else:
    print("Not eligible")