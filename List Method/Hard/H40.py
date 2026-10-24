scores = [71, 88, 45, 88]
scores.sort(reverse=True)  # [88 , 88 , 71 ,45]

if scores[0] == scores[1]:
    print("Top score is shared")
if scores[3] < 60:
    print( "No low score review")
else:
    print("Low score review")