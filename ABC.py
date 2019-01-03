import sys
nr1, nr2, nr3 = [int(x) for x in input().split()]
abc = sys.stdin.readline()

numbers = [nr1, nr2, nr3]
output = [""] * 3

output[abc.index("A")] = numbers[numbers.index(min(numbers))]
output[abc.index("C")] = numbers[numbers.index(max(numbers))]

numbers.sort()
output[abc.index("B")] = numbers[1]

print(*output)
