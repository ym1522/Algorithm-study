from sys import stdin
from collections import Counter
n = int(stdin.readline())
sn = list(map(int,stdin.readline().split()))
m = int(stdin.readline())
sm = list(map(int,stdin.readline().split()))

count = Counter(sn)

for i in range(m):
    if sm[i] in count:
        print(count[sm[i]], end=" ")
    else:
        print(0, end=" ")