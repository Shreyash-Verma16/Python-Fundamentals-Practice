names = ["Isha", "Nikhil", "Pari"]
status = ["present", "absent", "present"]

if "absent" in status:
    index = status.index("absent")
    status.pop(index)
    names.pop(index)

names.insert(1, "Zara")
status.insert(1, "present")

print(names)
print(status)