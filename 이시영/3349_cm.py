from sys import stdin
import math
n=int(stdin.readline())
a,b = map(int,stdin.readline().split())
sum=[]
mins=10000
check=0
if a>=0:
    for i in range(a):
        cc=math.sqrt(pow(i,2)+pow(n,2))/10 + math.sqrt(pow((i-a),2)+pow(b,2))/5
        if mins > cc:
            mins=cc
            check=i
else:
    for i in range(a,0):
        cc=math.sqrt(pow(i,2)+pow(n,2))/10 + math.sqrt(pow((i-a),2)+pow(b,2))/5
        if mins > cc:
            mins=cc
            check=i
print(check)