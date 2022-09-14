from sys import stdin

n=int(stdin.readline())
count=1
while True:
    if n==1:
        break
    if n%2==0:
        n=n/2
    else :
        n=3*n+1
    count+=1
print(count)