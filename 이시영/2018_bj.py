from sys import stdin

n = int(stdin.readline())

left, right=0,0
sum=0
count=0
while left <= right:
    if sum<n:
        right+=1
        sum+=right
    elif sum>n:
        sum-=left
        left+=1
    else:
        count+=1
        right+=1
        sum+=right
        
print(count)