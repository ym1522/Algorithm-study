# input()로 하면 시간초과가 생기기 때문에 sys.stdin.readline() 사용
from sys import stdin
for _ in range(3):
    n=int(stdin.readline())
    s=0
    for _ in range(n):
        m=int(stdin.readline())
        s+=m
    if s==0:
        print("0")
    elif s>0:
        print("+")
    else:
        print("-")