import sys

N, K = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))
scores = list(set(students))
scores.sort()

max_cnt = 0
P = max(scores) - 1
for score in scores[::-1]:
    prizes = [0] * N
    prizes[0] = int(students[0] >= score or (N > 1 and students[1] >= score))
    for i in range(1, N - 1):
        prizes[i] = int(students[i-1] >= score or students[i] >= score or students[i + 1] >= score)
    prizes[N-1] = int(students[N-1] >= score or (N > 1 and students[N-2] >= score))
        
    cnt = sum(prizes)
    if max_cnt < cnt and cnt <= K:
        P = score
        max_cnt = cnt
print(P)