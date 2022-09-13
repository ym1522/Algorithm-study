from sys import stdin
# 백트래킹
def asdf(a):
    if a == m:
        print(' '.join(map(str, arr)))
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            arr.append(i)
            asdf(a+1)
            visited[i]=False
            arr.pop()

n, m = map(int, stdin.readline().split())
visited=[False]*(n+1)
arr=[]
asdf(0)

''' # itertools 순열을 이용해 풀수있음
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())
arr = list(range(1,n+1))
ncm=itertools.permutations(arr,m)
for i in ncm:
    print(' '.join(map(str, i)))
'''
