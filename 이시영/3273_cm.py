from sys import stdin

n=int(stdin.readline())
print(n, end=" ")
while n!=1:
    if n%2==0:
        n= n/2
        print(int(n), end=" ")
    else:
        n= 3*n+1
        print(int(n), end=" ")