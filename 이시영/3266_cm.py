from sys import stdin

a=int(stdin.readline())

for i in range(a):
    n=int(stdin.readline())
    if n%2==0:
        print("R")
    else:
        print("L")