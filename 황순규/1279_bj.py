D, H, W = map(int, input().split())

x = (D**2 / (H**2 + W**2)) ** (1/2)
print(int(H*x), int(W*x))