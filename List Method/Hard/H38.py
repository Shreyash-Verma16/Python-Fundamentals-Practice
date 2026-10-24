boxes = ["standard-A", "fragile-B", "standard-C"]
b = input("Enter your weather : ")

if b == "rain" and "fragile-B" in boxes and "cover-B" not in boxes:
    boxes.insert(1, "cover-B")

print(boxes)

#used in ai in this 