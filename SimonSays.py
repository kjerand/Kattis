"""
cases = int(input())

for i in range(cases):
    text = input()
    words = text.split(" ")

    output = ""
    if words[0] == "simon" and words[1] == "says":
        for i in range(2, len(words)):
            output += words[i] + " "
    print(output)
"""

N = int(input())

for i in range(N):
    text = input()
    
    if text.startswith("simon says"):
        print(" ".join(text.split()[2:]))
    else:
        print()