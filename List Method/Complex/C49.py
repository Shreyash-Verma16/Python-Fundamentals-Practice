ledger = [500, -80, -120, 0]

valid = []
rejected = []
total = 0

if ledger[0] > 0 or (-100 <= ledger[0] <= -1):
    valid.append(ledger[0])
    total = total + ledger[0]
else:
    rejected.append(ledger[0])

if ledger[1] > 0 or (-100 <= ledger[1] <= -1):
    valid.append(ledger[1])
    total = total + ledger[1]
else:
    rejected.append(ledger[1])

if ledger[2] > 0 or (-100 <= ledger[2] <= -1):
    valid.append(ledger[2])
    total = total + ledger[2]
else:
    rejected.append(ledger[2])

if ledger[3] > 0 or (-100 <= ledger[3] <= -1):
    valid.append(ledger[3])
    total = total + ledger[3]
else:
    rejected.append(ledger[3])

print("valid =", valid)
print("rejected =", rejected)
print("net total =", total)