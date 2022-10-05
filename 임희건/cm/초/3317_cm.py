# 농부 민겸이는 밭에서 농사를 짓습니다.
# 민겸이의 밭은 N × N 크기의 정사각형 모양입니다. 즉, N^2개의 1 × 1 크기의 땅으로 나눌 수 있습니다. 각 땅은 빈 땅, 작물만 있는 땅, 잡초만 있는 땅으로 구분됩니다. 민겸이는 잡초를 손쉽게 제거하기 위해 최첨단 오리 농법을 도입했습니다.
# 오리 인덕이는 식탐이 많기 때문에 민겸이가 정한 어떤 가로줄 또는 세로줄의 잡초와 작물을 모두 먹습니다. 인덕이가 먹을 수 있는 양에 한계는 없습니다. 민겸이는 인덕이가 작물을 하나도 먹지 않도록 하며, 인덕이를 원하는 만큼 이용할 수 있습니다.
# 똑똑한 민겸이는 인덕이를 적절히 이용하여 모든 작물을 보존하면서 최대한 많은 잡초를 없앴습니다. 이때 잡초만 있는 땅이 몇 개 남아있는지 알려주는 프로그램을 작성해주세요.

import sys

ground = []
sum = 0

N = int(sys.stdin.readline())

for i in range(N):
    temp1 = list(map(int, sys.stdin.readline().split()))

    if 1 not in temp1:
        for j in range(N):
            temp1[j] = 0

    ground.append(temp1)

for k in range(N):
    temp2 = []

    for l in range(N):
        temp2.append(ground[l][k])

    if 1 not in temp2:
        for m in range(N):
            ground[m][k] = 0

for n in range(N):
    sum = sum + ground[n].count(2)

print(sum)