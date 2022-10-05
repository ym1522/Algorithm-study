from sys import stdin
a, b, c = map(int,stdin.readline().split())

def divide(x,y):
    if y==1:
        return x%c
    cnt=divide(x,y//2)
    if y%2==0:
        return (cnt*cnt)%c
    else:
        return (cnt*cnt*x)%c
print(divide(a,b))