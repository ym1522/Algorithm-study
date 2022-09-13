import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

print(A * int(B % 10))
print(A * int(B % 100 // 10))
print(A * int(B // 100))
print(A * B)