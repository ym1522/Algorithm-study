# 여름을 쾌적하게 보내기 위해서는 에어컨이 필요하다는 것에는 큰 이견이 없습니다. 그러나 에어컨의 목표 온도를 몇으로 정할지에 관해서는 의견이 충돌하는 경우가 잦습니다.
# 철수는 같은 공간에서 근무하는 회사원 N명의 의견을 수렴하여 에어컨의 목표 온도를 결정하려고 합니다. 최대한 많은 수의 회사원을 만족시킬 수 있는 에어컨의 목표 온도를 구하는 프로그램을 작성해주세요.
# 단, 조건을 만족하는 온도가 여러 개이면 그중에서 가장 낮은 온도가 정답이 됩니다.

# X

import sys

N = int(sys.stdin.readline())
air = [0] * 31

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())

    for j in range(s, e + 1):
        air[j] += 1

for k in range(31):
    if air[k] == max(air):
        print(k)

        break