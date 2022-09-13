# 최근 체중감량에 관심이 생긴 재승이는 항상 제로칼로리 음료를 찾습니다.
# 식품의약품안전처에 따르면, 음료의 100ml당 열량이 4kcal이하라면 제로칼로리라고 표기할 수 있습니다.
# 재승이가 구매한 음료의 용량과 열량이 주어지면 제로칼로리 음료라고 표기할 수 있는지 알려주세요.

import sys

N, M = map(float, sys.stdin.readline().split())

zero = M / N * 100

if zero <= 4:
    print("YES")
    
else:
    print("NO")