from sys import stdin

x = int(stdin.readline())
n = int(stdin.readline())
sum=0
for i in range(n):
    a, b = map(int,stdin.readline().split())
    sum+=a*b
if sum==x:
    print('Yes')
else:
    print('No')