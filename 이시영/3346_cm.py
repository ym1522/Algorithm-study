from sys import stdin
import itertools

n=input()
npr=itertools.permutations(n,len(n))

a=[''.join(i) for i in npr]
ch=0
for i in range(len(a)):
    if int(a[i])%13==0:
        ch=1
        break
    else:
        ch=0
if ch==1:
    print('YES')
else:
    print('NO')