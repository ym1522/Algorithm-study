from sys import stdin

n=int(stdin.readline())
asdf=list(map(int,stdin.readline().split()))
count={}
pr=[]
new_x=[]

for i in asdf:
    try:
        count[i]+=1
    except:
        count[i]=1
count=list(count.items())

for i in range(len(count)):
    if count[i][1]>=4:
        new_x.append(count[i][0])
        new_x.append(count[i][0])
    elif count[i][1]>=2:
        new_x.append(count[i][0])
        
for i in range(len(new_x)):
    for j in range(i+1,len(new_x)):
        pr.append(new_x[i]*new_x[j])
        
if pr:
    print(max(pr))
else:
    print(0)