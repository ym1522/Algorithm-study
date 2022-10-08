import sys

n = int(sys.stdin.readline())
arr=[]

for i in range(n):
    arr.append(sys.stdin.readline().rstrip().split())
    arr[i][0] = int(arr[i][0])      # 숫자를 int로 바꿔주지 않아 오류

arr.sort(key = lambda x: x[0])

for i in arr:
    print(*i)