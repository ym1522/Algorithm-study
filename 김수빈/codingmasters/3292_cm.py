import sys

H, W = map(int, sys.stdin.readline().split())
inputs = list(map(lambda x: x.strip(), sys.stdin.readlines()))
back = inputs[:H]
h, w = map(int, inputs[H].split())
img = inputs[H + 1:]

for i in range(H - h, H):
    back_str = back[i][W-w:]
    back[i] =  back[i][:W-w]+ ''.join(list(map(lambda x: x[0] if x[1] == '.' else x[1], zip(back_str, img[i - (H - h)]))))
print('\n'.join(back))