tasks = ["write", "review", "deploy"]
priority = "yes"
blocked  = "review"
NT = "test"

if blocked in tasks:
    tasks.pop(1)
if NT not in tasks:
    tasks.append(NT)
if priority == "yes":
    if "deploy" in tasks:
        b = tasks.pop(1)
        tasks.insert(0 ,b)
        print(tasks)
    else:
        print(tasks)
