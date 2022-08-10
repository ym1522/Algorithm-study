import sys

A = float(sys.stdin.readline())
print(A)
if A - int(A) > 0.1:
    print('bottom')
else:
    print('top')