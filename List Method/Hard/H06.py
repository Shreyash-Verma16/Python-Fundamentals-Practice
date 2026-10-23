topics = ["API", "Python", "Git"]
new_topics = ["Git", "SQL", "Docker"]

if new_topics[0] not in topics:
    topics.append(new_topics[0])

if new_topics[1] not in topics:
    topics.append(new_topics[1])

if new_topics[2] not in topics:
    topics.append(new_topics[2])

if "SQL" in topics:
    topics.remove("SQL")
    topics.insert(0, "SQL")

print(topics)