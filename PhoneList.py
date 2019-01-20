cases = int(input())
for i in range(cases):
    nr = int(input())
    numbers = []
    for j in range(nr):
        cell = int(input())
        numbers.append(cell)
    found = False
    for x in range(len(numbers)):
        counter = 0
        for y in range(len(numbers)):
            if str(numbers[y]).startswith(str(numbers[x])):
                counter += 1
        if counter == 2:
            found = True
    if found:
        print("NO")
    else:
        print("YES")
