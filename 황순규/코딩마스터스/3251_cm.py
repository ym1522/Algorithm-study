import sys

scores =  list(map(int, sys.stdin.readline().split()))

if min(scores) < 40 or sum(scores)/len(scores) < 60:
    print('F')
else:
    print('P')