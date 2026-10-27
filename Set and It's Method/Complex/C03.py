packed = {"charger", "mouse", "keyboard"}
required = {"charger", "mouse", "adapter"}

shared = packed.intersection(required)

print("Shared items:", shared)

if "adapter" in packed:
    print("Adapter ready")
else:
    print("Adapter missing")