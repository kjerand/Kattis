cases = int(input())

for i in range(cases):
    stores = int(input())
    read = input()
    positions = read.split()
    positions = list(map(int, positions))

    positions.sort()
    answer = (positions[len(positions) - 1] - positions[0]) * 2
    print(answer)