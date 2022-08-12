import sys
from functools import reduce
from fractions import Fraction

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

n, m = map(int, sys.stdin.readline().split())
try:
    print(Fraction(factorial(n), (factorial(m)*factorial(n-m))))
except:
    print(1)