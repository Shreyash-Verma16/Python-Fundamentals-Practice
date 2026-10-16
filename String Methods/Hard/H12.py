text = "error errors error"

count = text.count("error")

print(count, "substring matches")

# count() counts substrings, not whole words.
# Therefore "error" inside "errors" is counted too.