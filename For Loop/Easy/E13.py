text = 'a1b2c3d4'
count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print(count)