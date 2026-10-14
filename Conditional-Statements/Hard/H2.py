G  = float(input("Enter your GPA:"))
I  = float(input("Enter your icnome:"))
A = float(input("Enter Attendence"))

if G < 0 or G > 4.0 or I <0 or A > 100 or A < 0 :
    print("Invalid GPA or income or attendence")
elif G >= 3.7:
    print("Eligible")
elif G >= 3.5 and I <= 300000 and A >= 90:
    print("Eligible")
else:
    print("Not Eligible")

