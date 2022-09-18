from sys import stdin

def divide_paper(x,y,n):
    global arr
    ch=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != ch:
                for i in range(3):
                    for j in range(3):
                        divide_paper(x+i*(n//3), y+j*(n//3), n//3)
                return
    arr.append(ch)

n=int(stdin.readline())
paper=[list(map(int, stdin.readline().split())) for _ in range(n)]
arr=[]

divide_paper(0,0,n)
print(arr.count(-1))
print(arr.count(0))
print(arr.count(1))