from sys import stdin
n=int(stdin.readline())
count=0
for b in range(1,501):
    for a in range(b,501):
        if (a**2 - b**2)==n:
            count+=1
print(count)