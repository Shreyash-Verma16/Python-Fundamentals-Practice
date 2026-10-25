group_a = {"Mira", "Tara", "Aman"}
group_b = {"Tara", "Aman"}

a = group_a.union(group_b)
group_a.remove("Tara")
print(a)
print(group_a)