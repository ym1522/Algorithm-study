import sys

n = float(sys.stdin.readline())
if n == 0:
    print('bottom')
else:
    n /= 0.5
    if n % 2 == 0:
        print('bottom')
    else: print('top')