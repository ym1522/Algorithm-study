from sys import stdin

n, m = map(int, stdin.readline().split())
s = set()
check=0
for i in range(n):
    s.add(input())
for _ in range(m):
    ch=input()
    if ch in s:
        check+=1
print(check)