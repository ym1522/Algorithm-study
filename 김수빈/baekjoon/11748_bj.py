import sys

S = sys.stdin.readline().strip()
N = len(S)

# 이중 반복문으로 완전 탐색
str_set = set()
for i in range(N):
    for j in range(i, N):
        str_set.add(S[i:j + 1])
print(len(str_set))