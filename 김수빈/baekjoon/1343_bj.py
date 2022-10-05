import sys

def convert(board):
    answer = ""
    acc_x = ""
    for i, x in enumerate(board):
        if x == '.':
            if len(acc_x) == 0:
                answer += x
            else:
                alter = solution(len(acc_x), "AAAA", "BB")
                if alter is None: return "-1"
                answer += alter + x
            acc_x = ""
            continue
        acc_x += x
    if acc_x:
        alter = solution(len(acc_x), "AAAA", "BB")
        if alter is None: return "-1"
        answer += alter
    return answer

def solution(n, A_str, B_str):
    if n % 2 != 0 or n < 2: return None
    
    answer = ""        
    while n >= len(A_str):
        answer += A_str
        n -= len(A_str)
    while n >= len(B_str):
        answer += B_str
        n -= len(B_str)
    return answer

board = sys.stdin.readline().strip()
answer = convert(board)
print(answer)
