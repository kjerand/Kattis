import math
while True:
    try:
        text = input()
        letters = list(text)
        d = {}
        for i in range(len(letters)):
            if letters[i] in d:
                d[letters[i]] += 1
            else:
                d[letters[i]] = 1
        answer = math.factorial(len(letters))
        for x in d:
            answer //= math.factorial(d[x])
        print(answer)
    except EOFError:
        break