import sys

S = sys.stdin.readline().strip()
N = len(S)

suffix = []
for i in range(N):
    suffix += [S[i:]]
suffix.sort()
print('\n'.join(suffix))