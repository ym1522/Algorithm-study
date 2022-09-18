import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board += [list(sys.stdin.readline().strip())]
A, B = map(int, sys.stdin.readline().split())

board_gr = [[0 for _ in range(M)] for _ in range(N)]
board_oc = [[0 for _ in range(M)] for _ in range(N)]
board_ca = [[1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'g':
            board_gr[i][j] = 1

        if board[i][j] == 'o':
            for x in range(max(0, i - A), min(i + A + 1, N)):
                for y in range(max(0, j - A), min(j + A + 1, M)):
                    if abs(i - x) + abs(j - y) <= A:
                        board_oc[x][y] = 1
                        
        if board[i][j] == 'c':
            for x in range(max(0, i - B), min(i + B + 1, N)):
                for y in range(max(0, j - B), min(j + B + 1, M)):
                    if abs(i - x) + abs(j - y) <= B:
                        board_ca[x][y] = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if board_gr[i][j] * board_oc[i][j] * board_ca[i][j] > 0:
            cnt += 1
print(cnt)