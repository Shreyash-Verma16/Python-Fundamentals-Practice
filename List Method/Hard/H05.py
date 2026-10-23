scores = [0, 50, 100, -1]

valid = []

if scores[0] >= 0 and scores[0] <= 100:
    valid.append(scores[0])

if scores[1] >= 0 and scores[1] <= 100:
    valid.append(scores[1])

if scores[2] >= 0 and scores[2] <= 100:
    valid.append(scores[2])

if scores[3] >= 0 and scores[3] <= 100:
    valid.append(scores[3])

valid.sort()

print(valid)