'''   시간초과,,, 아무래도 하나씩 다 돌려봐서 그런듯
from sys import stdin
n=int(stdin.readline())
abc=list(map(int, stdin.readline().split()))
for i in range(1,min(abc)+1):
    count=0
    for j in range(n):
        if abc[j]%i==0:
            count+=1
    if count==n:
        print(i)
'''
from sys import stdin
from math import gcd
n=int(stdin.readline())
if n==2:
    a,b= map(int, input().split())
    gcd1=gcd(a,b)
if n==3:
    a,b,c= map(int, input().split())
    gcd1=gcd(gcd(a,b),c)

for i in range(1, gcd1//2+1):
    if gcd1%i==0:
        print(i)
print(gcd1)
