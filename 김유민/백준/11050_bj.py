from math import factorial
import sys

n, k = map(int, sys.stdin.readline().split())
res = factorial(n) / (factorial(k) * factorial(n-k))
print(int(res))