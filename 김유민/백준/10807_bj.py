import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
v = int(sys.stdin.readline())

count = 0
for i in arr:
    if v == i: count += 1

print(count)