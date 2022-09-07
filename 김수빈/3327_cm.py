import copy, sys

N = int(sys.stdin.readline())
board = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))

for i in range(N):
    nxt_board = copy.deepcopy(board)
    for r in range(5):
        for c in range(5):
            alive = 0
            for x, y in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                if x < 0 or y < 0 or x >= 5 or y >= 5: continue
                if board[x][y] == "1": alive += 1
            nxt_board[r][c] = "1" if alive == 3 else "0"
            nxt_board[r][c] = "1" if board[r][c] == "1" and alive == 2 else nxt_board[r][c]
    board = nxt_board

for j in range(5):
    print(''.join(board[j]))