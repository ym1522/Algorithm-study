import sys

while True:
    arr = list(map(int, sys.stdin.readline().split(' ')))
    arr.sort()
    if sum(arr) == 0: break
    print('right' if arr[0]**2 + arr[1]**2 == arr[2]**2 else 'wrong')