from sys import stdin
import itertools

n=int(stdin.readline())
num=list(map(int ,input().split()))
npr=itertools.combinations(num,4)
npr=list(npr)
ch=0
#a=[''.join(i) for i in npr]
for i in range(len(npr)):
    a=npr[i][0]*npr[i][1]
    aa=npr[i][2]*npr[i][3]
    b=npr[i][0]*npr[i][2]
    bb=npr[i][1]*npr[i][3]
    c=npr[i][0]*npr[i][3]
    cc=npr[i][1]*npr[i][2]
    if a==aa or b==bb or c==cc:
        ch=1
        break
    else:
        ch=0
if ch==1:
    print('YES')
else:
    print('NO')