from math import *

def fahrenheit_to_celcius(F):
    assert F >= -459.67, "F degree must be higher"
    C = (F - 32) * 5 / 9
    return C

def celsius_to_fahrenheit(C):
    assert C >= -273.15, "C degree must be higher"
    F = C * 9 / 5 + 32
    return F

def isalmost(n, m, d):
    return abs(n - m) <= d

def greatest_root(a, b, c):
    assert a != 0, "INVALID"
    delta = b * b - 4 * a * c
    if delta >= 0:
        return (-b + sqrt(delta)) / (2 * a)
    else:
        return None

def roots(a, b, c):
    assert a != 0, "INVALID"
    delta = b * b - 4 * a * c
    if delta >= 0:
        return ((-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a))
    else:
        return (None, None)    

# Conservation Celsius <==> Fahrenheit
assert isalmost(fahrenheit_to_celcius(-459.67), -273.15, 1e-13)
print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celcius(32))

# Prenons racine
print(greatest_root(1, 0, 3))
assert all(greatest_root(a, b, c) in roots(a, b, c) for a in range(-5, 6) if a != 0 for b in range(-5, 6) for c in range(-5, 6))