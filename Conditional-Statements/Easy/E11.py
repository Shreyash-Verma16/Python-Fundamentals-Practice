a = int(input("Enter a number: "))

if a %3 == 0 and a %7 == 0:
    print("Both when divisible by both, 3 only, 7 only")
else:
    print("Not divisible by both 3 and 7")