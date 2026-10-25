blocked_codes = {"A14", "B07"}
code = "B07"

if code in blocked_codes:
    print("Blocked")
else:
    print("Allowed")