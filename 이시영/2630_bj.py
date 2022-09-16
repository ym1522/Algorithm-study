from sys import stdin

def divide_paper(x,y,n):
    global white_count
    global blue_count
    count=0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j]:
                count+=1

    if count==n**2:
        blue_count+=1
    elif not count:
        white_count+=1
    else:
        divide_paper(x,y,(n//2))
        divide_paper(x+(n//2), y,(n//2))
        divide_paper(x,y+(n//2),(n//2))
        divide_paper(x+(n//2),y+(n//2),(n//2))
    return

n=int(stdin.readline())
paper=[list(map(int, stdin.readline().split())) for _ in range(n)]
white_count=0
blue_count=0

divide_paper(0,0,n)
print(white_count)
print(blue_count)