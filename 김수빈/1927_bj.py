import sys, heapq

N = int(sys.stdin.readline())
ops = list(map(int, sys.stdin.readlines()))
h = []
for op in ops:
    if op > 0:
        heapq.heappush(h, op)
    else:
        print(0) if not h else print(heapq.heappop(h))