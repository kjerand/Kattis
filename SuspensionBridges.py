import math
d, s = [int(x) for x in input().split()]

def a():
    a = math.pow(1, -4)
    found = True
    while found:
        if ((a * math.cosh(d / (2 * a))) - (a + s) < 0.0001):
            found = False 
        a += 0.001 
    return a 
a = a()

def l(a, d):
    return 2 * a * math.sinh(d / (2 * a))

answer = l(a, d)

print("%.4f" % answer)