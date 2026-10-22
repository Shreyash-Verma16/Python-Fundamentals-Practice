planned = ["milk", "rice", "tea"]
delivered = ["rice", "tea", "sugar"]

missing = []
unexpected = []

if planned[0] not in delivered:
    missing.append(planned[0])

if planned[1] not in delivered:
    missing.append(planned[1])

if planned[2] not in delivered:
    missing.append(planned[2])

if delivered[0] not in planned:
    unexpected.append(delivered[0])

if delivered[1] not in planned:
    unexpected.append(delivered[1])

if delivered[2] not in planned:
    unexpected.append(delivered[2])

print("missing =", missing)
print("unexpected =", unexpected)

#sure used ai in this ms copilot ``