group_a = {"Chess", "Robotics"}
group_b = {"Robotics", "Music"}
a = group_a.intersection(group_b)

if "Robotics" in a:
    print("Both groups offer Robotics")
else:
    print("Did not have robotics")