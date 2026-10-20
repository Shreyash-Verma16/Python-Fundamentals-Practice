messages = ["server DOWN!!!", "disk full", "backup delayed!"]

display = []

display.append(messages[0].replace("!!!", "!").capitalize())
display.append(messages[1].replace("!!!", "!").capitalize())
display.append(messages[2].replace("!!!", "!").capitalize())

print(display)

if display[2].endswith("!"):
    print("important: yes")
else:
    print("important: no")