from math import sqrt
from matplotlib import pyplot as plt
import numpy as np

def partition(a, b, n):
    step = (b - a) / n
    return [(a + step * i, a + step * (i + 1)) for i in range(n)]

assert partition(-1, 1, 1) == [(-1.0, 1.0)]
assert partition(0, 30, 3) == [(0.0, 10.0), (10.0, 20.0), (20.0, 30.0)]
assert partition(-1, 1, 4) == [(-1.0, -0.5), (-0.5, 0.0), (0.0, 0.5), (0.5, 1.0)]

def riemann(f, a, b, n = 100):
    return sum(f((x + y) / 2) * (y - x) for (x, y) in partition(a, b, n))

assert riemann(lambda x:x, 0, 1) == 0.5
assert abs(riemann(sqrt, 0, 1) - 2 / 3) < 1e-4

def primitive(f, x, n = 100):
    return riemann(f, 0, x, n)

assert all(primitive(lambda x:x, x) == x * x / 2 for x in [-32, 0, 1, 2, 8, 64])

def fprimitive(f, n = 100):
    return lambda x:primitive(f, x, n)

assert all(fprimitive(sqrt)(x) == primitive(sqrt, x) for x in range(100))

def f(x): return 2 * x
def g(x): return x**2 - 2
F = fprimitive(f)

x = np.linspace(-2, 2, 100)

npF = F(x)
npg = g(x)
npG = g(x) + 2

plt.figure(figsize = (12, 12))
plt.rcParams.update({'font.size': 14})

plt.plot(x, npF, 'b', label = 'f', linewidth = 4)
plt.plot(x, npg, 'r', label = 'g', linewidth = 1)
plt.plot(x, npG, 'black', label = 'g + 2', linewidth = 2)

plt.title('Visualise Exact and Approximated Primitives')
plt.legend(loc = 'best')
plt.axvline(0)
plt.axhline(0)

plt.show()