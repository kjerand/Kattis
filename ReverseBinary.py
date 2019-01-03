number = [int(x) for x in input().split()]
nr = number[0]

binary = format(nr, "b")
tmp = binary[::-1]
output = int(tmp, 2)

print(output)