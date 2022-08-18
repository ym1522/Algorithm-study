from sys import stdin
k=int(stdin.readline())
if k%2==0:
    n=k+2
else:
    n=k+1
while True:
    if ((n/2)%2)!=0:
        print(n)
        break
    else:
        n+=2
