names = ["Asha", "Ravi", "Meera"]
scores = [82, 49, 71]

qualified = []

if scores[0] >= 60:
    qualified.append(names[0])

if scores[1] >= 60:
    qualified.append(names[1])

if scores[2] >= 60:
    qualified.append(names[2])

print(qualified)