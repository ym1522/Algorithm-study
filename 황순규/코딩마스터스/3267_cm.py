import sys

x = int(sys.stdin.readline())

if x % 2 == 0:
    print(x - 1)
else:
    print(x + 1)