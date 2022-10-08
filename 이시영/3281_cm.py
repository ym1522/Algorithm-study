from sys import stdin

n,k=map(int,stdin.readline().split())
tv=list(map(int,stdin.readline().split()))
sum=[0]*(n-k+1)
for i in range(0,n-k+1):
    for j in range(k):
        if tv[i+j]==0:
            sum[i]=0
            break
        sum[i]+=tv[i+j]
if max(sum)==0:
    print("")
else:
    print(max(sum))