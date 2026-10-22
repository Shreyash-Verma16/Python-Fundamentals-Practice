labels = ["python_lists", "string_methods!", "logic_lab"]

display = []

display.append(labels[0].replace("_", " ").capitalize())
display.append(labels[1].replace("_", " ").capitalize())
display.append(labels[2].replace("_", " ").capitalize())

print(display)

if labels[1].endswith("!"):
    print("Attention: yes")
else:
    print("Attention: no")