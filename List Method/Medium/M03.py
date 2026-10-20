labels = ["phone-old", "tablet", "camera-old"]

cleaned = []

cleaned.append(labels[0].replace("-old", "").capitalize())
cleaned.append(labels[1].replace("-old", "").capitalize())
cleaned.append(labels[2].replace("-old", "").capitalize())

print(cleaned)
