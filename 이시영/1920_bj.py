# 이진 탐색으로 품. 그냥 for문으로 찾으면 시간초과
from sys import stdin

def search(target, data):
    start=0
    end=len(data)-1
    
    while start<=end:
        mid=(start+end)//2
        if data[mid]==target:
            return 1
        elif data[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return 0

n = int(stdin.readline())
na = sorted(list(map(int, stdin.readline().split())))

m = int(stdin.readline())
ma = list(map(int, stdin.readline().split()))

for i in ma:
    print(search(i, na))