import sys

a, b = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())

b -= y
if b < 0: b = 0

if a+b-x <= 0:
    print("YES")
else:
    print("NO")