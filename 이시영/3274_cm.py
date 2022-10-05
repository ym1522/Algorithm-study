from sys import stdin
n=int(stdin.readline())
if n%2==0:
    print("jjajangmyeon")
elif (n-1)%4==0:
    print("jjamppong")
else:
    print("bokkeumbap")