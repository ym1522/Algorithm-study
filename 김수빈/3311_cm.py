import sys

def solution(N, R, coord):
    coord_x = list(map(lambda x: x[0], coord))
    coord_y = list(map(lambda x: x[1], coord))

    min_x, max_x = min(coord_x), max(coord_x)
    min_y, max_y = min(coord_y), max(coord_y)

    board = [[0 for _ in range(min_y - R, max_y + R + 1)] for _ in range(min_x - R, max_x + R + 1)]
    for x, y in coord:
        for i in range(x - R, x + R + 1):
            for j in range(y - R, y + R + 1):
                if ((x - i) ** 2 + (y - j) ** 2) ** (1/2) <= R: 
                    board[i - min_x + R][j - min_y + R] += 1

    x, y = min_x - R, min_y - R
    k = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if k < board[i][j]:
                k = board[i][j]
                x, y = i + min_x - R, j + min_y - R
    return x, y

N, R = map(int, sys.stdin.readline().split())
coord = []
for _ in range(N):
    coord += [tuple(map(int, sys.stdin.readline().split()))]

x, y =solution(N, R, coord) 
print(x, y, sep=' ')