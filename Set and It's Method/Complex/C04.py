label = "PYTHON-basics"
tags = {"coding", "Python basics"}

label = label.replace("PYTHON", "Python")
label = label.replace("-", " ")
label = label.capitalize()

if label in tags:
    print("Already registered")
else:
    tags.add(label)

print("Final label:", label)
print("Tags:", tags)