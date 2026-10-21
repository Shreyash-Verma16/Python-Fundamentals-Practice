slots = [14, 9, 11]
cancelled_time = 9
display_order = "latest first"

if cancelled_time in slots:
    slots.remove(cancelled_time)

slots.sort()

if display_order == "latest first":
    slots.reverse()

print(slots)