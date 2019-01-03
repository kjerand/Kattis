import sys
cases = int(sys.stdin.readline().strip())

for y in range(cases):
    nr1, nr2, answer = [int(x) for x in input().split()]
    possible = False
    if nr1 + nr2 == answer:
        possible = True
    elif nr1 - nr2 == answer:
        possible = True
    elif nr2 - nr1 == answer:
        possible = True
    elif nr1 * nr2 == answer:
        possible = True
    elif nr1 / nr2 == answer:
        possible = True
    elif nr2 / nr1 == answer:
        possible = True
    if possible:
        print("Possible")
    else:
        print("Impossible")

