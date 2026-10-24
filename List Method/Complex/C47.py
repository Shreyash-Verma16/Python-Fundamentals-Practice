products = ["tea", "coffee", "rice", "soap"]
qty = [0, 5, -2, 8]

if -2 in qty:
    index = qty.index(-2)
    qty.pop(index)
    products.pop(index)

if 0 in qty:
    index = qty.index(0)
    qty.pop(index)
    products.pop(index)

if "salt" not in products:
    products.append("salt")
    qty.append(12)

if "soap" in products:
    index = products.index("soap")

    p = products.pop(index)
    q = qty.pop(index)

    products.insert(0, p)
    qty.insert(0, q)

print(products)
print(qty)
