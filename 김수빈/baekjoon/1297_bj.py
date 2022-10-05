import math

D, H, W = map(int, input().split())
x = ((D ** 2) / (H ** 2 + W ** 2)) ** 0.5

tv_h, tv_w = math.floor(x * H), math.floor(x * W)
print(f"{tv_h} {tv_w}")