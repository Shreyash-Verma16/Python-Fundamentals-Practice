log = ["A-start", "B-finish", "A-start", "C-end"]

if log[0] == log[2]:
    log.pop(2)
if log[2] == "C-end":
    print(log)
else:
    log.insert(3,"C-end")
    print(log)