labels = {"new", "review"}

if "review" in labels:
    labels.remove("review")
    print("Review Removed", labels)

if "urgent" not in labels:
    print("Missing")



