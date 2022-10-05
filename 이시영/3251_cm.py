from sys import stdin
n=list(map(int,stdin.readline().split()))
if n[0]>=40 and n[1]>=40 and n[2]>=40 and n[3]>=40 and n[4]>=40 and sum(n)/5>=60:
    print("P")
else:
    print("F")