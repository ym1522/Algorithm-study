from sys import stdin
import math

def num(x):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

n = int(stdin.readline())
if num(n)==True:
    print("clap")
else:
    print(n)