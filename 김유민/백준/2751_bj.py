import sys

n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
print(*arr, end='\n')