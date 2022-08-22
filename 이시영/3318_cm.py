from sys import stdin

def getdiv(n):
    divlist=[]
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            divlist.append(i)
            if i**2 != n:
                divlist.append(n//i)
    divlist.sort()
    del divlist[-1]
    return divlist

a,b=map(int,stdin.readline().split())

aa=getdiv(a)
bb=getdiv(b)
if sum(aa)==b and sum(bb)==a:
    print("YES")
else:
    print("NO")
