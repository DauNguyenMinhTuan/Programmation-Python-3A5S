# We All Float Down Here!
import numpy as np, matplotlib.pyplot as plt
from math import * 

# The Zero Ditchotomy
def di(f, a, b, d = 1e-16):
    if abs(f(a)) <= d:
        return a
    if abs(f(b)) <= d:
        return b
    while abs(a - b) > d:
        mid = (a + b) / 2
        if mid == a or mid == b: return mid
        # print(a, mid, b, abs(a-b), f(mid))
        if abs(f(mid)) <= d:
            return mid
        elif f(a) * f(mid) > 0:
            a = mid
        else:
            b = mid

# Recursive version
def di2(f, a, b, d = 1e-16):
    if abs(f(a)) <= d:
        return a
    if abs(f(b)) <= d:
        return b
    if abs(a - b) <= d:
        return a
    mid = (a + b) / 2
    if mid == a or mid == b: return mid
    if abs(f(mid)) <= d:
        return mid
    if f(a) * f(mid) > 0:
        return di2(f, mid, b, d)
    else:
        return di2(f, a, mid, d)

def g(x): return x ** 2 - 2

print(di(g, 1, 2))
print(di2(g, 1, 2))
print()

# This Is All Very Derirative...
def f(x): return 2 * x

def deriv(f, x, h = 0.01):
    return (f(x + h) - f(x - h)) / (2 * h)

def fderiv(f, h = 0.01):
    return lambda x: deriv(f, x, h)

G = fderiv(g)

def test_deriv():
    print(" x   f(x)  G(x)        f(x) - G(x)")
    x = -2.0
    while x <= 2.05:
        print("%4.1f %5.2f %5.2f   %.17f" % (x, f(x), G(x), f(x) - G(x)))
        x += 0.1

# test_deriv()

x = np.linspace(-2, 2, 100)
npf = f(x)
npg = g(x)
npG = G(x)

plt.figure(figsize = (12, 12))
plt.rcParams.update({'font.size': 18})

plt.plot(x, npf, 'b', label = 'f', linewidth = 4)
plt.plot(x, npG, 'r', label = 'G', linewidth = 1)
plt.plot(x, npg, 'black', label = 'g', linewidth = 3)

plt.title("Visualise Exact and Approximated Derivatives")
plt.legend(loc = 'best')
plt.axvline(0)
plt.axhline(0)

# plt.show()

def newton(f, x, eps = 1e-15):
    # print(fderiv(f)(x))
    while abs(f(x)) >= eps:
        assert fderiv(f)(x) != 0.0, "Cannot find root in this case!"
        print(x)
        x = x - (f(x) / fderiv(f)(x))
    return x

res = newton(g, 1)

print(res)
print(sqrt(2) - res)
print()