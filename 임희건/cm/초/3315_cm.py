# 앨라배마 해변 쥐(이하 해변 쥐)는 미국 앨라배마주 해변에 서식하는 설치류입니다.
# N행 M열의 격자로 구분된 N×M칸의 앨라배마주 해변 지도가 주어지면 해변 쥐가 살 수 있는 칸이 몇 개나 되는지 알려주는 프로그램을 작성해주세요.
# 해변 쥐가 살 수 있는 칸은 다음과 같습니다.
# 1. "땅" 칸이다. (바다에 살 수 없다)
# 2. 임의의 "바다" 칸과의 거리가 A와 같거나 작다. (해변에 서식한다)
# 3. 모든 "들고양이 서식지" 칸과의 거리가 B보다 크다. (들고양이는 천적이다)
# 어떤 두 칸 사이의 거리는 첫번째 칸이 x1행 y1열, 두번째 칸이 x2행 y2열일 때 |x2 - x1| + |y2 - y1|로 계산합니다.

# New

import sys

N, M = map(int, sys.stdin.readline().split())

field = []

for _ in range(N):
    temp1 = list(sys.stdin.readline())
    temp1 = temp1[:-1]

    field.append(temp1)

A, B = map(int, sys.stdin.readline().split())

check = []

for _ in range(N):
    temp2 = []

    for _ in range(M):
        temp2.append(0)

    check.append(temp2)

for i in range(N):
    for j in range(M):
        if field[i][j] == 'o':
            for k in range(N):
                for l in range(M):
                    if abs(i - k) + abs(j - l) <= A and field[k][l] != 'o' and field[k][l] != 'c' and check[k][l] != 2:
                        check[k][l] = 1

        elif field[i][j] == 'c':
            for m in range(N):
                for n in range(M):
                    if abs(i - m) + abs(j - n) <= B:
                        check[m][n] = 2

c = 0

for o in check:
    c += o.count(1)

print(c)