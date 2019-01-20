while True:
    try:
        nr1, nr2 = [int(x) for x in input().split()]
        print(abs(nr2 - nr1))
    except EOFError:
        break

