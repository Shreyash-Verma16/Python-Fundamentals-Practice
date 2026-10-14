X = float(input("Enter your coordinate: "))
Y = float(input("Enter your coordinate: "))

if X == 0 and Y == 0:
    print("Origin")

elif Y == 0:
    print("X-axis")

elif X == 0:
    print("Y-axis")

elif X > 0 and Y > 0:
    print("Quadrant I")

elif X < 0 and Y > 0:
    print("Quadrant II")

elif X < 0 and Y < 0:
    print("Quadrant III")

elif X > 0 and Y < 0:
    print("Quadrant IV")