read = input()
counter = 0
while read != -1:
    minutes, letter, answer = [str(x) for x in read.split()]
    if answer == "right":
        counter += 1

    read = input()