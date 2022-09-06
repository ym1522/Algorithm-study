# 가영이가 빨래를 널고 있습니다.
# 가영이의 집에는 옷걸이와 바지걸이가 있는데, 옷걸이에는 상의와 하의 구분 없이 빨래를 널 수 있지만 바지걸이에는 하의 빨래만 널 수 있습니다. 
# 가영이가 널어야 하는 상의 빨래와 하의 빨래의 개수가 주어지고, 가영이의 집에 있는 옷걸이와 바지걸이 개수가 주어질 때 가영이가 빨래를 모두 널 수 있는지 판단하는 프로그램을 작성해주세요

import sys

a, b = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())

b = b - y
    
if b < 0:
    b = 0
    
if a + b > x:
    print('NO')
        
else:
    print('YES')