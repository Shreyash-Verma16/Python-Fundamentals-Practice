pending = {"CASE-17"}

case_id = pending.pop()

print(case_id)

if case_id in pending:
    print("Still pending")
else:
    print("No longer pending")

print(pending)