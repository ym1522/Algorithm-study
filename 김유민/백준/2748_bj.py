import sys

n = int(sys.stdin.readline())
arr = [0, 1]

for i in range(n):
    arr.append(arr[i]+arr[i+1])
    
print(arr[n])