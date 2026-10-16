a = input("Enter yout file name : ")
b = a.endswith(( ".pdf",".png"))

if b == False:
    print("rejected")
else:
    print("Accepted")