import sys

k = int(sys.stdin.readline())
money = []
for i in range(k):
    money.append(int(sys.stdin.readline()))
res=[]
for m in money:
    if m != 0:
        res.append(m)
    else:
        res.pop()
print(sum(res))