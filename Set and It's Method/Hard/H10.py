A = {"C-01", "C-02"}
B = {"C-02", "C-03"}
target = "C-04"
all_ids = A.union(B)
if "C-04" in all_ids:
    all_ids.remove("C-04")
    print(all_ids)
else:
    print( "No matching ID")