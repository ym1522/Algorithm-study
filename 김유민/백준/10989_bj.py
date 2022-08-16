import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    n = int(sys.stdin.readline())
    arr[n] += 1

for index, i in enumerate(arr):
    if i == 0:
        pass
    else:
        for j in range(i):
            print(index)