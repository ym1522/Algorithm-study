from sys import stdin

n=int(stdin.readline())
arr=[list(map(int,stdin.readline().split())) for _ in range(n)]

for i in arr:
    if 1 not in i:
        for j in range(n):
            if i[j]==2:
                i[j]=0
    
count=0
for j in range(n):
    lis=[]
    for i in arr:  
        lis.append(i[j])
    if 1 in lis:
        for j in range(n):
            if lis[j]==2:
                count+=1
print(count)