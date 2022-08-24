import sys
import math

D, H, W = map(int, sys.stdin.readline().split())

tmp = D ** 2 / (H ** 2 + W ** 2)

h = math.floor(math.sqrt(tmp * H ** 2))
w = math.floor(math.sqrt(tmp * W ** 2))

print(h, w)