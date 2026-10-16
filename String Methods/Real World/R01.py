filename = input("Enter filename: ")

if filename.endswith((".pdf", ".png", ".jpg", ".jpeg")):
    print("Accepted")
else:
    print("Rejected")