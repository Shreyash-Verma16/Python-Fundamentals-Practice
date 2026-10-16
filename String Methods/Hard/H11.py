text = input("Enter text: ")

while "  " in text:
    text = text.replace("  ", " ")

print(text)