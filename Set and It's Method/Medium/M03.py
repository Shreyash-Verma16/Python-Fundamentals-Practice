devices = {"keyboard", "mouse", "monitor"}
target = "mouse"

if target in devices:
    devices.remove("mouse")
    print("Removed")
    print(devices)
else:
    devices.add("mouse")
    print("Not Listed")
    