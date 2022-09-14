from sys import stdin

n=int(stdin.readline())
fin=[0 for _ in range(n+1)]
fin[1]=1

for i in range(2,n+1):
    fin[i]=fin[i-1]+fin[i-2]

print(fin[-1])