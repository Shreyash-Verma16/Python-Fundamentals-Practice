codes = ["A12", "BAD", "B07"]
quantities = [3, 0, 5]

if "BAD" in codes:
    index = codes.index("BAD")
    codes.pop(index)
    quantities.pop(index)

print(codes)
print(quantities)