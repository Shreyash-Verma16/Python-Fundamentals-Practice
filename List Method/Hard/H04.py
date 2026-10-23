titles = ["refund pending", "fake!!!", "status update"]

titles[0] = titles[0].replace("fake", "flagged")
titles[1] = titles[1].replace("fake", "flagged")
titles[2] = titles[2].replace("fake", "flagged")

titles[0] = titles[0].replace("!!!", "!")
titles[1] = titles[1].replace("!!!", "!")
titles[2] = titles[2].replace("!!!", "!")

titles[0] = titles[0].capitalize()
titles[1] = titles[1].capitalize()
titles[2] = titles[2].capitalize()

print(titles)
#used ai in this 