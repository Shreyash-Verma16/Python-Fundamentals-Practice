text = "abababa"

count = text.count("aba")

print(count)

# "aba" can start at positions 0, 2, and 4 (3 overlapping matches).
# count() returns 2 because it counts only non-overlapping matches.