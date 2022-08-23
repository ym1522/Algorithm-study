import sys

a, b = map(int, sys.stdin.readline().split())
d_a = []
d_b = []

for i in range(1, a):
    if a % i == 0:
        d_a.append(i)

for i in range(1, b):
    if b % i == 0:
        d_b.append(i)

if sum(d_a) == sum(d_b):
    print('YES')
else:
    print('NO')
    
print(sum(d_a), sum(d_b))
