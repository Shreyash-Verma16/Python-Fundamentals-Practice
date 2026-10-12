age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age < 5:
    print("Free")
elif age <= 12:
    print("Child ticket INR 100")
elif age <= 59:
    print("Adult ticket INR 250")
else:
    print("Senior ticket INR 150")