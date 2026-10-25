access_a = {"read", "print"}
access_b = {"read", "write"}

a = access_a.union(access_b)

if "write" in a:
    a.remove("write")
    print(a)
    print("access_b is unchanged" ,access_b)
