from math import *
from operator import inv

# Warm-up
A = {'a', 'b', 'c', 'd'}
B = {1, 2, 3}
n = 100

print(sorted([(x, y) for x in A for y in B]))

squares = [i * i for i in range(1, int(sqrt(n)) + 1)]
assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Palindromes and other one-liners
def palindrome(s): return s == s[::-1]
assert palindrome('abba')
assert palindrome('abcba')
assert palindrome('')
assert palindrome('a')
assert not palindrome('ab')

def inverse(s): return [s[i] for i in range(len(s) - 1, -1, -1)]
assert inverse('abc') == ['c', 'b', 'a']
assert inverse('') == []

def palinv(s): return [c for c in s] == inverse(s)
assert palindrome('abba')
assert palindrome('abcba')
assert palindrome('')
assert palindrome('a')
assert not palindrome('ab')

def rmfrom(s, bad): return [c for c in s if c not in bad]
assert rmfrom('esope reste ici et se repose', 'aeiouy ') == ['s', 'p', 'r', 's', 't', 'c', 't', 's', 'r', 'p', 's']

def rmspaces(s): return rmfrom(s, ' ')
assert rmspaces ('esope reste ici et se repose ') == \
[ 'e', 's', 'o', 'p', 'e', 'r', 'e', 's', 't',
'e', 'i', 'c', 'i', 'e', 't', 's', 'e', 'r',
'e', 'p', 'o', 's', 'e']

def palindrome_sentence(s): return palinv(rmspaces(s))
assert palindrome_sentence('esope reste ici et se repose')
assert not palindrome_sentence('esope reste ici et se reposes')

def fsum(f, i, j): return sum(f(x) for x in range(i, j + 1))
assert fsum(lambda i: i, 0, 10) == 55
assert fsum(lambda i: i**2, 0, 10) == 385

# Prime numbers and sieve of Eratosthenes
def isprime(n): return (n > 1) and all(expr for expr in [n % i != 0 for i in range(2, max(2, int(sqrt(n)) + 1))])

comp = {i for i in range(1, n + 1) if any(i % j == 0 for j in range(2, max(2, int(sqrt(i)) + 1)))}
comp2 = {j for i in range(2, int(sqrt(n)) + 1) for j in range(i * 2, n + 1, i)}
comp3 = {i * j for i in range(2, int(sqrt(n)) + 1) for j in range(2, n // i + 1) if i * j <= n}
assert comp == comp2 == comp3, (comp ^ comp2, comp ^ comp3)

# Character ranges
def crange(a, b): return (chr(c) for c in range(ord(a), ord(b) + 1))
assert "".join(crange('A', 'Z')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert next(crange("a", "b")) == "a"

def charrange(*arg):
    while arg:
        assert len(arg) >= 2
        a, b, *arg = arg
        yield from crange(a, b)

assert "".join(charrange('A', 'Z', 'a', 'z', '0', '9')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
assert "".join(charrange()) == ''
assert next(charrange("a", "b")) == "a"