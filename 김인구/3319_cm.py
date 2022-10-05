# case4 failed

from decimal import *

p, q = map(float, input().split())

n = int(input())

getcontext().prec = n
result = Decimal(p) / Decimal(q)

if n < len(str(result)):
    print(result)
else:
    print(f'%.{n}f' % result)