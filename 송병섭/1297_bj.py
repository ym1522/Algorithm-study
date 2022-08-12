import sys
import math

a,b,c = map(int,sys.stdin.readline().split())
garo = a*c /(math.sqrt(b**2 + c**2))
sero = a*b /(math.sqrt(b**2 + c**2))
print(math.trunc(sero), math.trunc(garo))