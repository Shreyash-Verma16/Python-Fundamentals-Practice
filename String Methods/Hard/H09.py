template = "Welcome, <NAME>. Your profile is <NAME>."
b = input("Enter your name : ")

a = template.replace("<NAME>",b)

print(a)