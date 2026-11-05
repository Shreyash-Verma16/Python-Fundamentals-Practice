coding = {"Asha", "Dev", "Mira"}
design = {"Dev", "Mira", "Kabir"}

# Shared attendees
shared = coding.intersection(design)

# Combined roster
roster = coding.union(design)

# Add Nia
roster.add("Nia")

# Remove Kabir only if present
if "Kabir" in roster:
    roster.remove("Kabir")

print("Cleaned roster:", roster)
print("Shared attendees:", shared)