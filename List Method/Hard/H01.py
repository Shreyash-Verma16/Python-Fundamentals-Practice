stock = ["pen", "eraser", "glue"]
priority_mode = "yes"

if "eraser" in stock:
    stock.remove("eraser")

if "marker" not in stock:
    stock.append("marker")

stock.sort()

if priority_mode == "yes":
    stock.sort(reverse=True)

print(stock)