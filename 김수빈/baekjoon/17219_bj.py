import sys

# 주어진 사이트의 비밀번호 찾기
N, M = map(int, sys.stdin.readline().split())
# 딕셔너리 자료구조 활용
D = {}
for _ in range(N):
    url, pw = sys.stdin.readline().strip().split()
    D[url] = pw

for _ in range(M):
    url = sys.stdin.readline().strip()
    print(D[url])