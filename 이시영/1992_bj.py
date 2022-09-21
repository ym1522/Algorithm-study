from sys import stdin

def divide_tree(x,y,n):
    global arr
    ch=tree[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tree[i][j]!=ch:
                arr.append("(")
                divide_tree(x,y,(n//2))
                divide_tree(x,y+(n//2),(n//2))
                divide_tree(x+(n//2), y,(n//2))
                divide_tree(x+(n//2),y+(n//2),(n//2))
                arr.append(")")
                return
    arr.append(ch)

n=int(stdin.readline())
tree = [list(map(int,(input()))) for _ in range(n)]
arr=[]
divide_tree(0,0,n)
print("".join(map(str,arr)))