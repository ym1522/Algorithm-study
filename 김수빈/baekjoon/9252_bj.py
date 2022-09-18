import sys
import copy

# LCS (Longest Common Subsequence)
def solution(A, B, N):
    prevs = [""] * (N + 1)
    currs = [""] * (N + 1)

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                currs[j] = prevs[j - 1] + A[i - 1]
                continue

            if len(prevs[j]) >= len(currs[j - 1]):
                currs[j] = prevs[j]
            else:
                currs[j] = currs[j - 1]
        prevs = copy.deepcopy(currs)
    currs = sorted(currs, key=lambda x: len(x), reverse=True)
    return currs[0]

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

N = max(len(A), len(B))
seq = solution(A, B, N)
print(f"{len(seq)} {seq}")