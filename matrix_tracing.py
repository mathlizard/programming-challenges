# ---------------------------------------------------- 
# https://www.hackerrank.com/challenges/matrix-tracing 
# ---------------------------------------------------- 


import functools


@functools.lru_cache(maxsize=None)
def pow__mod_c(a, k, c):
    """computes a^k (mod c), 
       we assume a,k>=1, c > 1 integers"""
    
    if (k == 0):
        return 1
    elif (k & 1):
        return ((a * pow__mod_c(a, k//2, c)**2) % c)
    else:
        return ((pow__mod_c(a, k//2, c)**2) % c)


def n_choose_k__mod_c(n, k, c):
    """computes n choose k (mod c), when c is prime"""
    
    # numerator = ((n - k + 1) * (n - k + 2) * ... * (n)) (mod c)
    numerator = 1
    for i in range(n - k + 1, n + 1):
        numerator *= i
        numerator %= c
    
    # denominator = k! (mod c)
    denominator = 1
    for i in range(1, k + 1):
        denominator *= i
        denominator %= c
    
    # denominator = (k!)^-1 (mod c)
    # Fermat says (k!)^-1 (mod c) = (k!)^(c-2) (mod c), when c is prime;
    # therefore (k!)^-1 (mod c) = (k! (mod c))^(c-2) (mod c)
    denominator = pow__mod_c(denominator, c-2, c)
    
    # denominator is already inverted, so 
    # we just have to multiply the two together
    return ((numerator * denominator) % c)


T = int(input())
inputs = [input().split() for _ in range(T)]
A = [(int(x[0]), int(x[1])) for x in inputs]
c = (10**9) + 7


for m, n in A:
    print(n_choose_k__mod_c(m + n - 2, n - 1, c))
