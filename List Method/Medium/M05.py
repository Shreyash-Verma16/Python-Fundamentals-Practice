registered = ["Asha", "Dev"]
arrivals = ["Dev", "Mina", "Omar"]

if arrivals[0] not in registered:
    registered.append(arrivals[0])

if arrivals[1] not in registered:
    registered.append(arrivals[1])

if arrivals[2] not in registered:
    registered.append(arrivals[2])

print(registered)