# N × M 격자판이 흰색과 검은색 둘 중 하나로 색칠되어 있습니다.
# 격자판에서 검은색 직사각형의 개수를 출력하는 프로그램을 작성해주세요.
# ▢▢
# ■■
# 예를 들어 위와 같이 2x2 격자판이 색칠되어 있는 경우 검정색 직사각형의 개수는
# ■ : 2 개
# ■■ : 1 개
# 로 총 3개가 있습니다.

# 예제 입력1
# 2 2
# 00
# 11
# 예제 출력1
# 3

# 예제 입력2
# 3 3
# 111
# 111
# 111
# 예제 출력2
# 36

# 입력값 설명
# 첫 번째 줄에 두 정수 N, M(1 ≤ N, M ≤ 10)가 공백으로 구분되어 주어집니다.
# 두 번째 줄부터 N개의 줄에 걸쳐 격자판의 각 상태를 나타내는 M개의 숫자가 공백 없이 주어집니다
# 0은 흰색을 1은 검은색을 의미합니다

# 출력값 설명
# 검정색 직사각형의 개수를 출력하세요.

import sys
import numpy as np

N, M = map(int, sys.stdin.readline().split())    # 판 크기 입력
board = []    # 판 선언
count = 0    # 개수 선언

# 판 상태 입력
for _ in range(N):
    tmp = list(sys.stdin.readline())
    tmp = tmp[:-1]
    board.append(tmp)

# 확인할 직사각형 형태
for i in range(1, N + 1):
    for j in range(1, M + 1):

        # 직사각형 여부 확인
        for k in range(N - i + 1):
            for l in range(M - j + 1):
                tmp2 = []

                for m in range(k, k + i):
                    tmp2 = tmp2 + board[m][l : l + j]

                if not '0' in tmp2:
                    count += 1

# 개수 출력
print(count)