cd1, cd2 = [int(x) for x in raw_input().split()]
while cd1 != 0 and cd2 != 0:
    library = set(int(raw_input()) for i in range(cd1))
    counter = 0
    for i in range(cd2):
        if int(raw_input()) in library:
            counter += 1
    print(counter)
    cd1, cd2 = [int(x) for x in raw_input().split()]