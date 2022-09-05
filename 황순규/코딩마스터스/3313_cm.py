import sys

N = list(map(int, list(sys.stdin.readline().strip())))

if min(N) + max(N) == sum(N) / 2:
    print('YES')
else:
    print('NO')    
    