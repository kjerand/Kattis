cases = int(input())

for i in range(cases):
    nr = int(input())
    out = 1
    for i in range(1, nr + 1):
        out *= i
    out = str(out)[len(str(out))-1:]
    print(out)