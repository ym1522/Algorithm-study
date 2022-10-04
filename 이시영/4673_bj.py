from sys import stdin

def selfnumber(n):
    sum=n
    while n!=0:
        sum+=n%10
        n//=10
    return sum

check=[False]*10001
for i in range(1,10001):
    if selfnumber(i) <= 10000:   
        check[selfnumber(i)]=True
        
for i in range(1,10001):
    if check[i]==False:
        print(i)
