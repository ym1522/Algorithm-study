import sys

def solution(N, costs):
    values = [[0, 0, 0] for _ in range(N)]
    values[0] = costs[0]
    for i in range(1, N):
        for j in range(3):
            values[i][j] = min(values[i-1][:j] + values[i-1][j+1:]) + costs[i][j]

    return min(values[-1])

N = int(sys.stdin.readline())
costs = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
print(solution(N, costs))