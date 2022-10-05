import sys

arr = [0] * 10
cnt = 0

for i in range(10):
    arr[i]=int(sys.stdin.readline())
    arr[i] %= 42
    
print(len(set(arr)))