import math
r, c = [int(x) for x in input().split()]

area = r * r * math.pi

crustArea = (r - c)*(r - c)*math.pi
a = crustArea / area * 100
print("%.6f" % a)