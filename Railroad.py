import sys
read = sys.stdin.readline()
tmp = read.split(" ")
junctions = int(tmp[0])
switches = int(tmp[1])

print

if switches % 2 != 0:
    print("impossible")
else:
    print("possible")
