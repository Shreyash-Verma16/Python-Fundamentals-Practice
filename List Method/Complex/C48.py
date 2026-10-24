morning = ["Riya", "Aman", "Leena"]
afternoon = ["Aman", "Nikhil", "Riya"]

if afternoon[0] not in morning:
    morning.append(afternoon[0])

if afternoon[1] not in morning:
    morning.append(afternoon[1])

if afternoon[2] not in morning:
    morning.append(afternoon[2])

if "Leena" in morning:
    morning.remove("Leena")

if "Nikhil" in morning:
    morning.remove("Nikhil")
    morning.insert(0, "Nikhil")

print(morning)