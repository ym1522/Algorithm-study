# 첫째 줄에 TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W이 공백 한 칸을 사이에 두고 주어진다.
# 대각선 비율만 알면 됨
import sys
import math

d, h, w = map(int, sys.stdin.readline().split())
r = d/math.sqrt(h**2 + w**2)
print(int(r*h), int(r*w))