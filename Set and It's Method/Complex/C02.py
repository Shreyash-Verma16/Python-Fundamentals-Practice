team_a = {"read", "write", "export"}
team_b = {"read", "comment"}

access = team_a.union(team_b)

if "export" in access:
    access.remove("export")

if "write" in access:
    print("Write access remains")
else:
    print("Write access removed")

print("Access:", access)
print("Team A:", team_a)
print("Team B:", team_b)