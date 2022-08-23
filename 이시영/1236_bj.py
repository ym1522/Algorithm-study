from sys import stdin

n,m=map(int,stdin.readline().split())
cla=[list(map(str,stdin.readline().strip())) for _ in range(n)]
count1=0
count2=0
for i in cla:
    if 'X' not in i:
        count1+=1
        
for i in range(m):
    lis=[]
    for j in cla:
        lis.append(j[i])
    if 'X' not in lis:
        count2+=1
print(max(count1,count2))