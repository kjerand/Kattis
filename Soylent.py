import sys
import math
cases = int(sys.stdin.readline())

for i in range(cases):
    calories = int(sys.stdin.readline())

    if calories % 400 == 0:
        print(int(calories / 400))
    else:
        print(math.ceil(calories / 400))