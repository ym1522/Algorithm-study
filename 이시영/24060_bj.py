from sys import stdin

def merge_sort(A, i,j):
    if i<j:
        m=(i+j)//2
        merge_sort(A,i, m)
        merge_sort(A,m+1, j)
        merge(A,i,m+1,j)

def merge(A,i,m,j):
    global k
    global ans
    p=i
    q=m
    t=0
    tmp=[0]*(j-i+1)
    while p<m and q<=j:
        k-=1
        if A[p]>A[q]:
            tmp[t]=A[q]
            q+=1
        else:
            tmp[t]=A[p]
            p+=1
        if k==0:
            ans=tmp[t]
        t+=1
        
    while p<m:
        tmp[t]=A[p]
        k-=1
        if k==0:
            ans=tmp[t]
        p+=1
        t+=1
    while q<=j:
        tmp[t]=A[q]
        k-=1
        if k==0:
            ans=tmp[t]
        q+=1
        t+=1
    p=i
    i=0
    while p<=j:
        A[p]=tmp[i]
        p+=1
        i+=1

n,k=list(map(int,stdin.readline().split()))
A=list(map(int,stdin.readline().split()))
ans=-1
merge_sort(A,0,n-1)
print(ans)