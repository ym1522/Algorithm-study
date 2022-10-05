import sys

a , b = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

max_num = -1e9

for i in range(a - b + 1):
    if 0 in arr[i : i+b]:
        continue
    
    else:
        if sum(arr[i : i+b]) > max_num:
            max_num = sum(arr[i : i+b])
            
print(max_num)