users = ["admin_7", "riya2026!", "team_admin", "aman2026"]

accepted = []
rejected = []

if "admin" in users[0] or users[0].endswith("!"):
    rejected.append(users[0])
else:
    accepted.append(users[0])

if "admin" in users[1] or users[1].endswith("!"):
    rejected.append(users[1])
else:
    accepted.append(users[1])

if "admin" in users[2] or users[2].endswith("!"):
    rejected.append(users[2])
else:
    accepted.append(users[2])

if "admin" in users[3] or users[3].endswith("!"):
    rejected.append(users[3])
else:
    accepted.append(users[3])

print("accepted =", accepted)
print("rejected =", rejected)