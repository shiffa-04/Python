import math
ab = int(input())
bc = int(input())

degree_symbol = "\u00B0"

theta = math.degrees(math.atan(ab/bc))
round_theta = round(theta)

print(f"{round_theta}{degree_symbol}")
