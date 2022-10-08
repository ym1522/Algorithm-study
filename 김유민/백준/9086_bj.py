import sys

n = int(sys.stdin.readline())
str = []

for i in range(n):
    str.append(sys.stdin.readline().rstrip())

for i in range(n):
    print(str[i][0], end=''); print(str[i][-1])