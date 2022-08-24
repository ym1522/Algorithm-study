import sys

N = int(sys.stdin.readline())
list = []

for i in range(N):
    n = int(sys.stdin.readline())
    list.append(n)

list.sort()

for j in list:
    print(j)