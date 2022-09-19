import sys

n = int(sys.stdin.readline())

plane = [[0 for j in range(2)] for i in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split(' '))
    plane[i][0] = x
    plane[i][1] = y

plane.sort( key = lambda x: (x[1], x[0]) )

for i in range(n):
    print(plane[i][0], plane[i][1])