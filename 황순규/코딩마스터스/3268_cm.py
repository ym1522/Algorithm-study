import sys

A = float(sys.stdin.readline())
if A - int(A) > 0.1:
    print('bottom')
else:
    print('top')