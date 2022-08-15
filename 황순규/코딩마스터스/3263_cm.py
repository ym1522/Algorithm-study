import sys

N, M = map(int, sys.stdin.readline().split())

if M/N*100 <= 4:
    print("YES")
else:
    print("NO")