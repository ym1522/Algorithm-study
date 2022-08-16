from sys import stdin
import math
a, b=map(int, stdin.readline().split())

if a<30:
    if b<30:
        print(int(math.fabs(a-b)))
    else:
        print(min((b-a), (a+60-b)))
else:
    if b>30:
        print(int(math.fabs(a-b)))
    else:print(min((a-b), (b+60-a)))