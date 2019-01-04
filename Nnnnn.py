import math
nr = int(input())

def binarySearch(lower, upper):
    middle = (lower + upper) // 2
    value = middle * len(str(middle))
    if value == nr:
        return middle
    elif value + 1 == nr:
        return middle
    elif value < nr:
        return binarySearch(middle, upper)
    elif value > nr:
        return binarySearch(lower, middle)

k = binarySearch(0, nr)
print(k)
