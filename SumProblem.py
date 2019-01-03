import sys
cases = int(sys.stdin.readline())

for i in range(cases):
    test, number = [int(x) for x in input().split()]

    s3 = number * (number + 1)
    s1 = int(s3 / 2)
    s2 = number * number
    
    
    print(test, " ", s1, " ", s2, " ", s3)


    
