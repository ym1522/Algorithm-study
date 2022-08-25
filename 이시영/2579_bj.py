from sys import stdin

n=int(stdin.readline())
cc=[0]*301
sum=[0]*301
for i in range(n):
    cc[i]=int(stdin.readline())
   
sum[0]=cc[0]
sum[1]=max((cc[0]+cc[1]), (cc[1]))
sum[2]=max((cc[0]+cc[2]), (cc[1]+cc[2]))

for i in range(3,n):
    sum[i]=max((sum[i-2]+cc[i]), (sum[i-3]+cc[i-1]+cc[i]))
print(sum[n-1])