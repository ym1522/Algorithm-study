from sys import stdin
import math
money=int(stdin.readline())
money=1000-money
co=0
a=[500,100,50,10,5,1]
for i in a:
    if money//i:
        co+=(money//i)
        money=money%i
print(co)