filename = input("Enter filename: ")

if filename.endswith((".csv", ".json")):
    print("Accepted")
else:
    print("Rejected")