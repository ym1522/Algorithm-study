import sys

sys.setrecursionlimit(10 ** 9)
def solution(N, board, i, j):
    # 1 x 1 크기일 경우
    if N == 1: 
        if board[i][j] == 1: return (0, 1)
        return (1, 0)
    
    # board 안에 한가지 색깔만 가지는 경우
    val = board[i][j]
    cond_1 = True
    for x in range(i, i + N):
        for y in range(j, j + N):
            if board[x][y] != val:
                cond_1 = False
                break
        if not cond_1: break
    
    if cond_1:
        if val == 1: return (0, 1)
        return (1, 0)
    
    # 2 x 2로 나눔
    N = N // 2
    result = [0, 0]
    for x in range(2):
        for y in range(2):          
            blue, white = solution(N, board, x * N + i, y * N + j)
            result[0] += blue
            result[1] += white
    return result


N = int(sys.stdin.readline())
board = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

answer = solution(N, board, 0, 0)
print(answer[0])
print(answer[1])
