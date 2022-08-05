import sys

def solution(A, B, C):
    scores = [[[0] * (len(C) + 1) for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            for k in range(1, len(C) + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    scores[i][j][k] = scores[i - 1][j - 1][k - 1] + 1
                    continue
                cand = max([scores[i-1][j-1][k], scores[i-1][j][k], scores[i][j-1][k], scores[i][j][k-1]])
                scores[i][j][k] = cand
    return scores[-1][-1][-1]

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

print(solution(A, B, C))