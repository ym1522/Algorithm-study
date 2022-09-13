from sys import stdin

def asdf(a):
    if a == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1,n+1):
        visited[i]=True
        arr.append(i)
        asdf(a+1)
        visited[i]=False
        arr.pop()

n, m = map(int, stdin.readline().split())
visited=[False]*(n+1)
arr=[]
asdf(0)
