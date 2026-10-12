total = float(input("Enter order total: "))
member = input("Are you a member? (yes/no): ")

if total < 0:
    print("Invalid order total")
elif total >= 1000 or (member == "yes" and total >= 500):
    print("Free Shipping")
else:
    print("Shipping INR 80")