import sys


# LCS (Longest Common Subsequence) 알고리즘

def solution(A, B, N):
    prevs = [0] * (N + 1)
    currs = [0] * (N + 1)

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                currs[j] = prevs[j - 1] + 1
            else:
                currs[j] = max(prevs[j], currs[j - 1])
        prevs = currs.copy()
    return max(currs)

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

N = max(len(A), len(B))
print(solution(A, B, N))

