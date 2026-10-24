names = ["Asha", "Kabir", "Mina", "Zoya"]
marks = [78, -1, 92, 35]

passed = []
failed = []

if -1 in marks:
    index = marks.index(-1)
    marks.pop(index)
    names.pop(index)

if marks[0] >= 40:
    passed.append(names[0])
else:
    failed.append(names[0])

if marks[1] >= 40:
    passed.append(names[1])
else:
    failed.append(names[1])

if marks[2] >= 40:
    passed.append(names[2])
else:
    failed.append(names[2])

print("passed =", passed)
print("failed =", failed)