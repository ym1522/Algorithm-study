from sys import stdin

n=int(stdin.readline())
a=list(map(int,stdin.readline().split()))
if sum(a)>=100:
    print("0")
else:
    print(100-sum(a))