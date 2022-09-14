from sys import stdin

def asdf(a):
    if a == n:
        print(' '.join(map(str, arr)))
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            arr.append(i)
            asdf(a+1)
            visited[i]=False
            arr.pop()
        
n = int(stdin.readline())
visited=[False]*(n+1)
arr=[]
asdf(0)