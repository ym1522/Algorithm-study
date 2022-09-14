import sys
from functools import reduce
costs = [1000, 1500, 2000, 3000, 5000]

counts = list(map(int, sys.stdin.readline().split()))
costs = [costs[i] * counts[i] for i in range(5)]
print(reduce(lambda x, y: x + y, costs))