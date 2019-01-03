dice1, dice2 = [int(x) for x in input().split()]

counter = [0] * (dice1 + dice2)

for x in range(dice1):
    for y in range(dice2):
        counter[x + y] += 1

max = counter[0]
for x in counter:
    if x > max:
        max = x

for index in range(len(counter)):
    if counter[index] == max:
        print(index + 2)