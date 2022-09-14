# 빛의 삼원색은 빨간색(R), 초록색(G), 파란색(B)입니다.
# 삼원색 중 서로 다른 두 가지 색을 1:1로 합성하면 다음과 같은 결과를 얻을 수 있습니다.
# - 빨간색(R) + 초록색(G) ⇒ 노란색(Y)
# - 초록색(G) + 파란색(B) ⇒ 청록색(C)
# - 파란색(B) + 빨간색(R) ⇒ 자홍색(M)
# 단, 같은 색 두 개를 합성할 경우 색이 변하지 않습니다.
# 삼원색 정보를 담고 있는 N x M 크기의 배열 a, b를 합성하여 배열 c를 만든다고 합시다. 배열 c의 크기는 배열 a, b의 크기와 같습니다. 배열 a, b, c의 i번째 행, j번째 열에 위치한 색을 a_ij, b_ij, c_ij로 나타낼 때, c_ij는 a_ij와 b_ij를 합성한 색이 됩니다.
# 두 개의 배열이 주어졌을 때, 두 배열을 합성하여 새로운 배열을 만드는 프로그램을 작성해주세요.

import sys

a, b, c, line = [], [], [], []

N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    line = list(sys.stdin.readline().split())
    a.append(line)

for j in range(N):
    line = list(sys.stdin.readline().split())
    b.append(line)

for k in range(N):
    temp = []

    for l in range(M):
        if a[k][l] == b[k][l]:
            temp.append(a[k][l])

        elif a[k][l] == "R" and b[k][l] == "G":
            temp.append("Y")

        elif a[k][l] == "G" and b[k][l] == "R":
            temp.append("Y")

        elif a[k][l] == "G" and b[k][l] == "B":
            temp.append("C")

        elif a[k][l] == "B" and b[k][l] == "G":
            temp.append("C")

        elif a[k][l] == "B" and b[k][l] == "R":
            temp.append("M")

        elif a[k][l] == "R" and b[k][l] == "B":
            temp.append("M")

    c.append(temp)
    
for m in range(N):
    print(*c[m])