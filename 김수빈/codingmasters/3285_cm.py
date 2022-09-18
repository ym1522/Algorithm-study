import sys

N = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
coord = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

dists = list(map(lambda c: abs(x- c[0]) + abs(y - c[1]), coord))
print(min(dists) * 100)