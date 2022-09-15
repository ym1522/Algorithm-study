import sys
from functools import reduce

N, M, X = map(int, sys.stdin.readline().split())
matrix = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

answer = "NO"
for x in range(N):
    for y in range(M):
        accs = [[0 for i in range(M)] for j in range(N)]
        for i in range(x, N):
            for j in range(y, M):
                if (i, j) == (x, y): accs[i][j] = matrix[i][j]
                elif i == x:
                    accs[i][j] = accs[i][j - 1] + matrix[i][j]
                elif j == y:
                    accs[i][j] =  accs[i - 1][j] + matrix[i][j]
                else:
                    accs[i][j] = accs[i][j - 1] + accs[i - 1][j] + matrix[i][j] - accs[i - 1][j - 1]

        accs = list(reduce(lambda u, w: u + w, accs))
        if X in accs:
            answer = "YES"
            break

print(answer)