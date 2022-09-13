from sys import stdin

s=int(stdin.readline())

count=0
sum=1
while True:
    if s==0:
        break
    if s-sum<0:
        break
    else:
        s-=sum
        sum+=1
    count+=1
print(count)