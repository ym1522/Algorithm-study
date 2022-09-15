# -*- coding: utf-8 -*-
import sys

def lcs(N, A, B):
    prev_scores = [0] * (N + 1)
    cur_scores = [0] * (N + 1)

    for i in range(1, len(A)+ 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                cur_scores[j] = prev_scores[j - 1] + 1
            else:
                cur_scores[j] = max(prev_scores[j], cur_scores[j - 1])
        prev_scores = cur_scores.copy()
    return max(cur_scores)

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

N = max(len(A), len(B))
lcs_val = lcs(N, A, B)
print("YES") if len(B) == lcs_val else print("NO")