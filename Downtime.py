import operator
import math
requests, capacity = [int(x) for x in input().split()]
req = []
for i in range(requests):
    req.append(int(input()))

d = {}
for i in range(len(req)):
    for i in range(req[i]):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

max = max(d.items(), key=operator.itemgetter(1))[0]
servers = math.ceil(d[max] / capacity)

print(servers)

