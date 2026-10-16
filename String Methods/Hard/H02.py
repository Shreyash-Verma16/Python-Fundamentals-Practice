FN = input("Enter your file name : ")
B = FN.endswith((".py",".pyw",".ipynb"))
if B == True:
    print("Accepted")
else:
    print("Flase")