from sys import stdin

x,y=map(int,stdin.readline().split())
n=int(stdin.readline())
touch=[]
touch.append(y)
for i in range(n):
    a,b=map(int,stdin.readline().split())
    if a in touch:
        touch.append(b)
    elif b in touch:
        touch.append(a)
print(len(set(touch)))