from sys import stdin
import itertools

n, s = map(int,stdin.readline().split())
arr=list(map(int,stdin.readline().split()))
count=0
for i in range(1, n+1):
    com=itertools.combinations(arr,i)
    for j in com:
        if sum(j) == s:
            count+=1
print(count)