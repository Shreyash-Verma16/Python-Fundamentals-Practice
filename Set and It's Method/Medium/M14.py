first = {"A-1", "A-2"}
second = {"B-1"}
requested = "A-3"
a = first.union(second)

if requested in a:
    print("Ticket found")
else:
    print( "Ask the organizer")