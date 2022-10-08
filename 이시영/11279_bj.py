# heapq는 최소 힙으로 구현이 되어 있으므로 입력 값에 음수를 취해줌
from sys import stdin
import heapq

que=[]
n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    if x == 0 :
        if que:
            print(-1*heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, -1*x)