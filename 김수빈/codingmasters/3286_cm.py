import sys

N, A, B, C =  map(int, sys.stdin.readline().split())
airs = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

winds = [[-1 if (i, j) in airs else 0 for j in range(1, N + 1)] for i in range(1, N + 1)]
answer = set()
for i, j in airs:
    for x in range(max(i - 1 - B, 0), min(i - 1 + B, N - 1) + 1):
        if winds[x][j - 1] >= 0: winds[x][j - 1] += 1
        if winds[x][j - 1] >= C: answer.add((x, j - 1))
    for x in range(max(j - 1 - B, 0), min(j - 1 + B , N - 1) + 1):
        if winds[i - 1][x] >= 0: winds[i - 1][x] += 1
        if winds[i - 1][x] >= C: answer.add((i - 1, x))
print(len(answer))