code = "INV-TBD-2026"

if "TBD" in code:
    code = code.replace("TBD", "A17")

if code.endswith("2026"):
    code = code.replace("2026", "ARCHIVE")

print(code)