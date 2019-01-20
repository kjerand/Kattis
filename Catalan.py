import math

def catalan(number):
    #calc = (1//(number + 1))*((math.factorial(2*number))//(math.factorial(number)*math.factorial(2*number - number)))
    calc = math.factorial(2*number)//(math.factorial(number + 1) * math.factorial(number))
    return  calc

cases = int(input())
for i in range(cases):
    nr = int(input())
    out = int(catalan(nr))
    print(out)


