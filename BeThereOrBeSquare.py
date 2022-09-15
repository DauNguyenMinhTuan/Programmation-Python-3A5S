from math import *

# The Easy Way: isqrt_builtin
def isqrt_builtin(n):
    return floor(sqrt(n))

assert [ isqrt_builtin(n) for n in range(30) ] == \
    [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
      3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5 ]

# 