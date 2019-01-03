"""
import sys
read = sys.stdin.readline().strip()
input = read.split(" ")
syllables = int(input[0])
players = int(input[1])
"""
syllables, players = [int(x) for x in input().split()]

def solve():
    list = [2] * players
    playerIndex = [0] * players
    for x in range(len(list)):
        playerIndex[x] = x + 1
    index = 0

    while len(list) != 1:
        index += syllables - 1
        while index >= len(list):
            index = index - len(list)

        if list[index] == 2:
            list[index] = 1
            list.insert(index + 1, 1)
            playerIndex.insert(index + 1, playerIndex[index])
        elif list[index] == 1:
            list[index] = 0
            index += 1
        elif list[index] == 0:
            del list[index]
            del playerIndex[index]
    print(playerIndex[0])


# Main 
solve()

   
    
