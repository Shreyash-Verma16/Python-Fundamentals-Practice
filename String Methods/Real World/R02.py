log = "INFO: start | ERROR: timeout | INFO: retry | ERROR: failed"

count = log.count("ERROR")
index = log.find("ERROR")

if count == 0:
    print("No ERROR found")
else:
    print("Count:", count)
    print("First index:", index)