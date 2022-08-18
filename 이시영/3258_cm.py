from sys import stdin
n=int(stdin.readline())
aa=0
bb=0
for i in range(n):
    a, b=map(int,stdin.readline().split())
    if a==1:
        if b==2:
            bb+=1
        elif b==3:
            aa+=1
    elif a==2:
        if b==1:
            aa+=1
        elif b==3:
            bb+=1
    else:
        if b==1:
            bb+=1
        elif b==2:
            aa+=1
print(aa, bb)