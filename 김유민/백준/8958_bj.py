import sys
n = int(sys.stdin.readline())

for i in range(n):
    arr = list(sys.stdin.readline().rstrip())
    arr = list(map(lambda x: 1 if x=='O' else 0, arr))
    cnt = 0

    for j in range(len(arr)):
        if arr[j] == 1: 
            cnt += 1
            arr[j] = cnt
        else: cnt = 0

    print(sum(arr))