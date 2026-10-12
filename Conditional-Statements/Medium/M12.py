L = input("Are you logged in? (yes/no): ")
A = input("Are you an admin? (yes/no): ")

if L == "no":
    print("Please log in")
elif A == "yes":
    print("Admin dashboard")
else:
    print("User dashboard")