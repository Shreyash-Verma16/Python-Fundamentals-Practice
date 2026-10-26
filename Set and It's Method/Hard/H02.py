seniors = {"Asha", "Dev", "Mira"}
mentors = {"Dev", "Mira"}

a = seniors.intersection(mentors)

seniors.remove("Dev")

print("shared" , a)
print(seniors)