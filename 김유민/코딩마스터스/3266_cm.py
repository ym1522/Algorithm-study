import sys

n = int(sys.stdin.readline())

for i in range(n):
    number = int(sys.stdin.readline())
    if number % 2 == 0:
        print('R')
    else: print('L')