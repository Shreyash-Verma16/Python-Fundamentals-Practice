queue = ["T-12:normal", "T-07:critical", "T-22:high"]
RT = "T-12:normal"
NT = "T-31:critical"
maintenance_mode = "no"

if RT in queue:
    index = queue.index(RT)
    queue.pop(index)

if NT not in queue:
    if NT.endswith(":critical"):
        queue.insert(0, NT)
    else:
        queue.append(NT)

if maintenance_mode == "yes":
    queue.reverse()

print(queue)
