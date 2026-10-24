readings = [12, -3, 12, 5]
latest_first = "yes"

if -3 in readings:
    readings.remove(-3)

readings.sort()

if latest_first == "yes":
    readings.reverse()

print(readings)