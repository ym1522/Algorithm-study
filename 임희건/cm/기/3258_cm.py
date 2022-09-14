# 민겸이와 동훈이는 가위바위보 세계선수권 대회의 결승전에서 만났습니다.
# 드디어 때가 왔고, 민겸이와 동훈이는 여러 번의 가위바위보를 합니다. 민겸이와 동훈이는 각 가위바위보에서 이길 때마다 점수를 1점씩 얻습니다.
# 여러 번의 가위바위보가 진행된 후 민겸이와 동훈이가 얻은 점수를 구하세요.

import sys

N = int(sys.stdin.readline())

a_score, b_score = 0, 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1 and b == 3:
        a_score += 1

    elif a == 3 and b == 1:
        b_score += 1

    elif a > b:
        a_score += 1

    elif a < b:
        b_score += 1
        
print(a_score, b_score)