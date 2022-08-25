from sys import stdin
import math       # a**b이 아닌 pow(a,b)을 하면 시간초과가 안생김.
                  # a**b는 시간복잡도가 o(n)이지만 pow는 o(1)이기 때문
t=int(stdin.readline())

for _ in range(t):
    a,b=map(int,stdin.readline().split())
    ans=pow(a,b,10)
    if ans==0:
        print(ans+10)
    else:
        print(ans)