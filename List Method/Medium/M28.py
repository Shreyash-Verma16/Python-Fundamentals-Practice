products = ["pen", "lamp", "mug"]
prices = [20, 500, 150]

if "lamp" in products:
    index = products.index("lamp")  
    products.pop(index)             
    prices.pop(index)             
print(products)
print(prices)