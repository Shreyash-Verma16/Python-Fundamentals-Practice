confirmed = {"Ravi", "Tia"}
walk_ins = {"Uma", "Ravi"}
late_guest = "Neel"

confirmed.add(late_guest)
b = walk_ins.union(confirmed)
print(confirmed)
print(b)