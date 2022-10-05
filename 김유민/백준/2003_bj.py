import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start, end, cnt = 0, 0, 0
# print(sum(a[start:end+1]))

while True:
    if sum(a[start:end+1]) < m: end+=1
    if sum(a[start:end+1]) == m: cnt += 1; start += 1
    if sum(a[start:end+1]) > m: start += 1
    if end == len(a): break
print(cnt)