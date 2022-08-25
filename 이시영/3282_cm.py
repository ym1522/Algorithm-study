from sys import stdin

n,m=map(int,stdin.readline().split())
a=[[0]*100 for i in range(100)]
for i in range(n):
    a[i]=list(map(int,stdin.readline().split()))
    
asdf=[]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            sum=a[0][0]+a[0][1]+a[1][0]
        elif i==0 and j==m-1:
            sum=a[0][m-1]+a[0][m-2]+a[1][m-1]
        elif i==n-1 and j==0:
            sum=a[n-1][0]+a[n-1][1]+a[n-2][0]
        elif i==n-1 and j==m-1:
            sum=a[n-1][m-1]+a[n-1][m-2]+a[n-2][m-1]
        elif i==0:
            sum=a[0][j]+a[0][j-1]+a[0][j+1]+a[1][j]
        elif i==n-1:
            sum=a[n-1][j]+a[n-1][j-1]+a[n-1][j+1]+a[n-2][j]
        elif j==0:
            sum=a[i][0]+a[i-1][0]+a[i+1][0]+a[i][1]
        elif j==m-1:
            sum=a[i][m-1]+a[i-1][m-1]+a[i+1][m-1]+a[i][m-2]
        else:
            sum=a[i][j]+a[i-1][j]+a[i][j-1]+a[i][j+1]+a[i+1][j]
        asdf.append(sum)
print(max(asdf))