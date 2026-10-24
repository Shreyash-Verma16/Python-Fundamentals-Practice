message = "Call 555-0101 or 555-0101"

count = message.count("555-0101")

message = message.replace("555-0101", "555-0199")

print(message)

if count == 2:
    print("Two references updated")