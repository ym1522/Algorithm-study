from sys import stdin
import heapq

que=[]
n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    if x == 0 :
        if que:
            print(heapq.heappop(que)[1])
        else:
            print(0)
    else:
        heapq.heappush(que, (abs(x), x))  
# 튜플로 넣으면 앞의 값 기준 정렬 즉, 절대값을 씌운 x를 기준으로 정렬