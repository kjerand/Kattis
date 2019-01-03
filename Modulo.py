import sys
modulo = []
for i in range(10):
    number = int(sys.stdin.readline())
    found = False
    for i in range(len(modulo)):
        if modulo[i] == number % 42:
            found = True
    if found == False:
        modulo.append(number % 42)

print(len(modulo))
