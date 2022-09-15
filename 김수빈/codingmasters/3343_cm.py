import sys, copy
from functools import reduce

def get_next(N, board, i, j):
    for y in range(j, N):
        if board[i][y] == '.':
            return i, y
    
    for x in range(i, N):
        for y in range(N):
            if board[x][y] == '.':
                return x, y
    return N, N

def solution_bfs(N, board):
    get_key = lambda brd: '/'.join(list(reduce(lambda x, y: x + y, brd)))
    blank = list(reduce(lambda x, y: x + y, board)).count('.')
    if blank % 2 > 0: return 0

    cnt = 0
    prev = []
    i, j = get_next(N, board, 0, 0)
    cases = [(copy.deepcopy(board), get_key(board), i, j)]
    while cases:
        brd, key, i, j = cases.pop()
        if key in prev: continue
        prev += [key]

        if key.count('.') == 0:
            cnt += 1
            continue
        
        if brd[i][j] == '.':
            if i < N - 1 and brd[i + 1][j] == '.':
                tmp = copy.deepcopy(brd)
                tmp[i][j], tmp[i + 1][j] = f'h', f'h'
                tmp_key = get_key(tmp)
                nxt_i, nxt_j = get_next(N, tmp, i, j)
                cases += [(tmp, tmp_key, nxt_i, nxt_j)]
                        
            if j < N - 1 and brd[i][j + 1] == '.':
                tmp = copy.deepcopy(brd)
                tmp[i][j], tmp[i][j + 1] = f'v', f'v'
                tmp_key = get_key(tmp)
                nxt_i, nxt_j = get_next(N, tmp, i, j)
                cases += [(tmp, tmp_key, nxt_i, nxt_j)]
    return cnt
    
N = int(sys.stdin.readline())
board = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))

print(solution_bfs(N, board))