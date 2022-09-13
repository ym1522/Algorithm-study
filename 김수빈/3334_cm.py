import sys

def search_bfs(board, N, M, answer):
    cases = [(i, j, [(i, j)], answer[1:]) for i in range(N) for j in range(M) if board[i][j] == answer[0]]
    prev = []
    first_coord = []
    while cases:
        i, j, indices, answer = cases.pop()
        prev += [indices]
        if not answer: 
            first_coord += [indices[0]]
            continue
        
        if i > 0 and not (i - 1, j) in indices:
            if (not indices + [(i - 1, j)] in prev) and board[i - 1][j] == answer[0]:
                cases += [(i - 1, j, indices + [(i - 1, j)], answer[1:])]

        if i < N - 1 and not (i + 1, j) in indices:
            if (not indices + [(i + 1, j)] in prev) and board[i + 1][j] == answer[0]:
                cases += [(i + 1, j, indices + [(i + 1, j)], answer[1:])]

        if j > 0 and not (i, j - 1) in indices:
            if (not indices + [(i, j - 1)] in prev) and board[i][j - 1] == answer[0]:
                cases += [(i, j - 1, indices + [(i, j - 1)], answer[1:])]

        if j < M - 1 and not (i, j + 1) in indices:
            if (not indices + [(i, j + 1)] in prev) and board[i][j + 1] == answer[0]:
                cases += [(i, j + 1, indices + [(i, j + 1)], answer[1:])]
    return len(set(first_coord))
    
answer = sys.stdin.readline().strip()
N, M = map(int, sys.stdin.readline().split())
board = list(map(lambda x: x.strip(), sys.stdin.readlines()))
K = len(answer)

blanks = len(list(filter(lambda x: x == '.', ''.join(board))))
if N * M - K == blanks:
    print(search_bfs(board, N, M, answer))
else:
    print(0)
    

