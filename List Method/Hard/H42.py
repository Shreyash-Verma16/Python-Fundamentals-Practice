route = ["Hub", "Zone-C", "Zone-A", "Zone-B"]
blocked = "Zone-C"
express ="yes"

if blocked in route:
    route.pop(1)

if express == "yes":
    last = route.pop()
    route.insert(0 ,last)
    print(route)