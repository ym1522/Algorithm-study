import sys
import math

a,b,c = map(int,sys.stdin.readlines())
garo = a*c /math.sqrt(a**2 + b**2)
sero = a*b /math.sqrt(a**2 + b**2)
print(math.trunc(sero), math.trunc(garo))