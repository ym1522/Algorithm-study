import sys

N, M = map(int, sys.stdin.readline().split())
inputs = list(sys.stdin.readlines())
totals = [0] * (N + 1)
for i in range(M):
    cost, num = map(int, inputs[2 * i].split())
    people = inputs[2 * i + 1].split()
    avg_cost = cost // num
    for p_i in people:
        totals[int(p_i)] += avg_cost
        
print(' '.join(list(map(str, totals[1:]))))