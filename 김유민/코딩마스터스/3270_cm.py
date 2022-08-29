import sys

a, b = map(int, sys.stdin.readline().split(' '))
x, y = map(int, sys.stdin.readline().split(' '))

if a > x:
    print('NO')
elif (b-y)+a > x:
    print('NO')
else: print('YES')