import sys
sys.setrecursionlimit(10000)
def dfs(y,x):
    if x<0 or x>=w or y<0 or y>=h:
        return False
    if graph[y][x]==1:
        graph[y][x]=0
        dfs(y,x-1)  # 상하좌우
        dfs(y,x+1)
        dfs(y+1,x)
        dfs(y-1,x)
        
        dfs(y-1,x-1) # 대각선
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True
    return False

while(True):
    w, h = map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph=[list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    
    count=0
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                count+=1
    print(count)