from sys import stdin
import heapq

que=[]
n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    if x == 0 :
        if que:
            print(heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, x)