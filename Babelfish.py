import sys
str = sys.stdin.readline().strip()
d = {}

while str != "":
    words = str.split(" ")
    d[words[1]] = words[0]
    str = sys.stdin.readline().strip()

str = sys.stdin.readline().strip()
while str != "":
    if str in d:
        print(d.get(str))
    else:
        print("eh")
    str = sys.stdin.readline().strip()

