from math import *

# The Easy Way: isqrt_builtin
def isqrt_builtin(n):
    return floor(sqrt(n))

assert [ isqrt_builtin(n) for n in range(30) ] == \
    [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
      3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5 ]

# Racine carree entiere, the hard way!

def isqrt_hard(n):
    res = 0
    while((res + 1) * (res + 1) <= n):
        res += 1
    return res

assert [ isqrt_hard(n) for n in range(30) ] == \
    [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
      3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5 ]

def isqrt_sum(n):
    res = 0
    sum = 0
    while sum + 2  * res + 1 <= n:
        res += 1
        sum += 2 * res - 1
    return res

assert [ isqrt_sum(n) for n in range(30) ] == \
    [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
      3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5 ]

def isqrt_dicho(n):
    res = 0
    l = 0
    r = n
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == n: return mid
        elif mid * mid > n:
            r = mid - 1
        else:
            res = mid
            l = mid + 1
    return res

assert [ isqrt_dicho(n) for n in range(30) ] == \
    [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
      3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5 ]