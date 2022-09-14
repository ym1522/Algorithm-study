import sys

def solution(N, M, board, answer):
    min_count = -1
    for i in range(N - 7):
        for j in range(M - 7):
            count = 0
            for x in range(8):
                for y in range(8):
                    if board[i + x][j + y] != answer[x][y]:
                        count += 1
            min_count = count if min_count < 0 or count < min_count else min_count
    return min_count

D = {'W' : 0, 'B' : 1}
N, M = map(int, sys.stdin.readline().split())
board = list(map(lambda x: list(map(lambda y: D[y], x.strip())), sys.stdin.readlines()))

row = [1, 0] * 4
row_inv = [0, 1] * 4
answer = [row, row_inv] * 4
answer_inv = [row_inv, row] * 4

print(min(solution(N, M, board, answer), solution(N, M, board, answer_inv)))
