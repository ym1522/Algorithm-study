# python말고 pypy3으로 제출함 
from sys import stdin

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
k = int(stdin.readline())


count=0

for i in range(n):
    sum=0
    end=i
    while end<n:
        sum+=a[end]
        if sum>k:
            count+=(len(a)-end)
            break
        end+=1
print(count)