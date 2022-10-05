import sys

t = int(sys.stdin.readline())
arr = [[0 for j in range(2)] for i in range(t)]

for i in range(t):
    n, s = sys.stdin.readline().rstrip().split(' ')
    arr[i][0] = n
    arr[i][1] = s

for i in range(t):
    for j in arr[i][1]:
        print(j * int(arr[i][0]), end='')
    print()