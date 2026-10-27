morning = {"Asha", "Dev", "Mira"}
afternoon = {"Dev", "Kabir"}
paid = {"Dev", "Mira", "Kabir"}

# Combine sign-ups
roster = morning.union(afternoon)

# Add Tara
roster.add("Tara")

# Remove Mira if present
if "Mira" in roster:
    roster.remove("Mira")

# Keep only paid attendees
eligible = roster.intersection(paid)

# Check Dev
if "Dev" in eligible:
    print("Dev is eligible")
else:
    print("Dev is not eligible")

print("Eligible set:", eligible)
print("Morning:", morning)
print("Afternoon:", afternoon)
print("Paid:", paid)