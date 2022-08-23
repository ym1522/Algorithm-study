# 수열  -->  성공
import sys
arr = []
n = int(sys.stdin.readline())

arr.append(n)
while True:
    if n == 1: break 
    
    if n % 2 == 0:
        arr.append(n//2)
        n = n//2
    else: 
        arr.append(3*n+1)
        n = 3*n+1
    
    # if n == 1: break  <-- 여기 아님. 초항이 1일 때 안됨

print(len(arr))