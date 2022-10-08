import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

arr = [0] * 10

n = str(a*b*c)
for i in n:
    arr[int(i)] += 1

print(*arr, sep='\n')