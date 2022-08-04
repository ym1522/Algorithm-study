# 대각선의 법칙을 이용, X**2 + y**2 = z**2, 비율도 x:y=a,b일때 x*b=y*a를 이용
import math

D, H, W = map(int, input().split())

a=(D*H)/math.sqrt(W**2 + H**2)
b=math.sqrt(D**2 - a**2)

print(math.floor(a), math.floor(b))