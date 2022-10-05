# N개의 통에 사탕이 담겨 있습니다. 치훈이는 다음 2가지 연산을 이용해 모든 통에 들어있는 사탕의 개수가 같게 만드려고 합니다.
# 1. 임의의 통에 있는 사탕을 하나 먹는다.
# 2. 임의의 통에 있는 사탕을 다른 통으로 옮긴다.
# 이 때, 필요한 연산의 최소 횟수를 출력하는 프로그램을 작성해주세요.

# 예제 입력1
# 3
# 5 2 3
# 예제 출력1
# 2

# 예제 입력2
# 5
# 10 8 2 9 1
# 예제 출력2
# 9

# 입력값 설명
# 첫 번째 줄에 N이 주어집니다. (1 ≤ N ≤ 100)
# 두 번째 줄에 a_i가 공백으로 구분되어 주어집니다. (0 ≤ a_i ≤ 1,000)

# 출력값 설명
# 필요한 연산의 최소 횟수를 출력합니다.

import sys

N = int(sys.stdin.readline())    # 통 N개
a_i = list(map(int, sys.stdin.readline().split()))   # 사탕 a_i개

count = 0    # 연산 횟수
a_i_avg = sum(a_i) // N    # 각 통에 담길 목표 사탕 개수

# 임의의 통에 있는 사탕을 하나 먹는다
while sum(a_i) != a_i_avg * N:
    tmp = a_i.index(max(a_i))
    a_i[tmp] -= 1
    count += 1

# 임의의 통에 있는 사탕을 다른 통으로 옮긴다
while max(a_i) != min(a_i):
    tmp_max = a_i.index(max(a_i))
    tmp_min = a_i.index(min(a_i))
    a_i[tmp_max] -= 1
    a_i[tmp_min] += 1
    count += 1

# 연산 횟수 출력
print(count)