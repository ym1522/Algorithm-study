from sys import stdin

n=int(stdin.readline())
sum=[0]*(n+1)

for i in range(2,n+1):
    sum[i]=sum[i-1]+1
    if i%3==0:
        sum[i]=min(sum[i],sum[i//3]+1)
    if i%2==0:
        sum[i]=min(sum[i],sum[i//2]+1)
print(sum[n])