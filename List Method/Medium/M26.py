queue = ["Aman", "Riya", "Kunal"]
cancelled = "Aman"
vip = "Riya"

if cancelled in queue:
    queue.remove(cancelled)

if vip in queue:
    queue.remove(vip)
    queue.insert(0, vip)
else:
    queue.insert(0, vip)

print(queue)