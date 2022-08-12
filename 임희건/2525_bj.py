import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

A = A + C // 60
B = B + C % 60

if B >= 60:
    A = A + B // 60
    B = B % 60

if A >= 24:
    A = A % 24

print(A, B)