import sys

ml, kc = map(int, sys.stdin.readline().split(' '))

if ml // 25 >= kc:
    print('YES')
else: print('NO')