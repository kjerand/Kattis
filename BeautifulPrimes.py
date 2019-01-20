cases = int(input())

for i in range(cases):
    nr = int(input())
    x = 1
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors 

    while True:
        factors = prime_factors(x)
        result = 1
        for tmp in factors:
            result *= tmp
        if len(str(result)) == nr and len(factors) == nr:
            print(*factors, sep=' ')
            break
        x += 1


"""
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
"""