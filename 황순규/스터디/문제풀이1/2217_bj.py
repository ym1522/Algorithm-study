import sys

N = int(sys.stdin.readline())

ropes = [int(sys.stdin.readline()) for _ in range(N)]
ropes.sort()

weights = []
for i in range(len(ropes)):
    weights.append(ropes[i] * (N-i))

print(max(weights))
