# 농부 가영이는 텃밭에 울타리를 두르려고 합니다. 가영이의 텃밭은 가로가 a, 세로가 b인 직사각형 모양의 텃밭입니다.
# 가영이는 이 텃밭에 각 꼭짓점에 말뚝을 하나씩 박고,
# 그 사이에 몇 개의 말뚝을 박으려고 합니다. 가영이는 말뚝 사이가 너무 멀거나 가깝지 않았으면 좋겠다고 생각하여 말뚝 사이의 최대한의 거리 D와 최소한의 거리 d를 정했습니다. 
# 가영이의 텃밭의 가로 길이 a, 세로 길이 b와 말뚝 사이의 최대한의 거리 D, 최소한의 거리 d가 주어질 때, 가영이가 박을 수 있는 말뚝 개수의 범위를 구하는 프로그램을 작성해주세요.

# 예제 입력1
# 10 20 5 2
# 예제 출력1
# 12 30

# 예제 입력2
# 10 10 4 3
# 예제 출력2
# 12 12

# 입력값 설명
# 첫 번째 줄에 문제에서 설명한 자연수 a, b, D, d가 공백으로 구분되어 주어집니다. (1 ≤ a, b ≤ 10¹⁸, 1 ≤ d ≤ D ≤ 10¹⁸)

# 출력값 설명
# 위 조건을 만족하게 말뚝을 박을 수 없다면 -1을 출력합니다.
# 그렇지 않다면 가영이가 박을 수 있는 말뚝 개수의 최솟값과 최댓값을 공백으로 구분하여 출력합니다.

# 완벽히 해결 못 했음;

import sys
import math

a, b, D, d = map(int, sys.stdin.readline().split())

a_min = math.ceil(a / D)
b_min = math.ceil(b / D)
a_max = math.floor(a / d)
b_max = math.floor(b / d)

if a // a_min >= a // a_max and b // b_min >= b // b_max and d < a and d < b and D < a and D < b:
    pile_min = 2 * (a_min - 1) + 2 * (b_min - 1) + 4
    pile_max = 2 * (a_max - 1) + 2 * (b_max - 1) + 4

    print(pile_min, pile_max)

else:
    print(-1)