import sys
cd1, cd2 = [int(x) for x in input().split()]
while cd1 != 0 and cd2 != 0:
    library = []
    counter = 0
    #Legger til alle CD'ene til første personen i listen 'library'
    for i in range(cd1):
        cd = int(sys.stdin.readline())
        library.append(cd)

    def binarySearch(alist, item):
        first = 0
        last = len(alist)-1
        found = False

        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        
        return found

    #Bruker binærsøk til å sjekke om CD'ene til person 2 finnes i 'library' listen
    for i in range(cd2):
        cd = int(sys.stdin.readline())

        #Teller opp
        if binarySearch(library, cd):
            counter += 1
    print(counter)
    cd1, cd2 = [int(x) for x in input().split()]


