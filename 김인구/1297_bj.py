'''
대각선 D, 높이 비율 H, 너비 비율 W

TV의 높이, TV의 너비
-----------------------------------------
x에 대한 높이 비율 h, x에 대한 너비 비율 w

z^2 = D

z^2 = (x*W)^2 + (x*H)^2
z^2 = x^2(H^2 + W^2)
x^2 = z^2 / (H^2 + W^2)
x = z / sqrt(H^2 + W^2)
'''
import math
d, h, w = map(int, input().split())

x = d / math.sqrt(h**2 + w**2)
print(math.floor(h*x), math.floor(w*x))