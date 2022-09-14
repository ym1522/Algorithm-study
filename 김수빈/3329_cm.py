import sys

board = list(map(lambda x: list(map(int, x.strip())), sys.stdin.readlines()))

x, y = 0, 0
for i in range(10):
    if 2 in board[i]:
        x, y = i, board[i].index(2)
        break

limit = 3
idx = 2
cur_d = -1
directions = [(+1, 0), (0, -1), (-1, 0), (0, 1)]

while limit > 0:
    tmp_x, tmp_y = x + directions[idx][0], y + directions[idx][1]
    if tmp_x < 0 or tmp_x >= 10 or tmp_y < 0 or tmp_y >= 10: break
    if board[tmp_x][tmp_y] == 1:
        idx += cur_d
        idx  = idx if idx >= 0 else idx + 4
        idx = idx if idx < 4 else idx % 4
        cur_d *= -1
        limit -= 1
    else:
        board[x][y] = 0
        board[tmp_x][tmp_y] = 2
        x, y = tmp_x, tmp_y
        limit = 3

print("no") if limit == 0 else print("yes")