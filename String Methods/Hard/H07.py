text = "error at line 5; error at line 9"

a = text.find("error")
b = text.find("error", a + 1)

print(b)