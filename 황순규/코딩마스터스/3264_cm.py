import sys

A, B, C = map(int, sys.stdin.readline().split())

if A**2 <= (B**2)*C:
    print("YES")
else:
    print("NO")