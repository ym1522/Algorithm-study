import sys

def solution(N):
    if N == 1: return [[1]]
    prev = solution(N - 1)
    
    for i in range(N):
        if len(prev) > i: prev[i] += [0 for _ in range(N - len(prev[i]))]
        else: prev += [[0 for _ in range(N)]]

    cur = []
    for i in range(N):
        row = []
        for j in range(i + 1) :            
            row += [prev[i][j] + prev[i - 1][j] + prev[i - 1][j - 1]]
        cur += [row]
    return cur
    
N = int(sys.stdin.readline())
cur = solution(N)
answer = ""
for row in cur[::-1]:
    answer = answer + ' '.join(list(map(str, row))) + "\n"
print(answer[:-1])