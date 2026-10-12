a = input("Enter a character: ")

if a.isalpha():
    if a.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif a.isdigit():
    print("Digit")
else:
    print("Other")