import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    if N % 2 == 1:
        print('L')
    else:
        print('R')