import sys
import heapq

N = int(sys.stdin.readline())
h = []
D = {}
for n in range(N):
    num = int(sys.stdin.readline())
    if num in D:
        D[num] = D[num] + 1
    else:
        D[num] = 1
        heapq.heappush(h, num)
        
while h:
    n = heapq.heappop(h)
    for m in range(D[n]):
        print(n)