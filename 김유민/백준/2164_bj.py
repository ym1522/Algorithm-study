# 2164 - 카드2
# 메모리: 49284KB, 시간: 280ms

import sys
from collections import deque

# --- 시도 1: 시간 초과 ---
# n = int(sys.stdin.readline())
# arr = []
# for i in range(1, n+1): arr.append(i)

# while len(arr) > 1:
#     arr.pop(0)
#     arr.append(arr[0])
#     arr.pop(0)
# print(*arr)

n = int(sys.stdin.readline())
q = deque()
for i in range(1, n+1): q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q[0])
    q.popleft()
print(q[0])

'''
list로 큐의 효과를 내기는 좋지 X
  - list는 무작위 접근 (random access)에 최적화된 자료 구조이기 때문에 pop(0), insert(0, x)는 불리한 연산
  - 첫 번째 데이터 제거 후 뒤에 있는 데이터들을 한 칸씩 당겨줘야 함 (insert도 마찬가지)
'''