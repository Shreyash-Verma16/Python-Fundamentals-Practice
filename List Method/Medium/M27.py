filename = "report-FINAL-draft"

if "draft" in filename:
    filename = filename.replace("draft", "review")

if filename.endswith(".tmp"):
    label = "Temporary"
else:
    label = "Review file"

print(filename)
print(label)