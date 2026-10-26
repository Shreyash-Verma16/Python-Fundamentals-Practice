morning = {"visitor", "staff-1"}
evening = {"staff-1", "staff-2"}

a = morning.union(evening)
if "visitor" or "staff-2" in a:
    a.remove("visitor")
    a.remove("staff-2")
    print(a)
