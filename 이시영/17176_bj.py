from sys import stdin
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
chk = list(stdin.readline().strip())
arr.sort()
num=[]
for i in range(len(chk)):
    if 'a' <= chk[i] and chk[i] <='z':
        num.append(ord(chk[i])-ord('a')+27)
    elif 'A' <= chk[i] and chk[i] <= 'Z':
        num.append(ord(chk[i])-ord('A')+1)
    elif ' '==chk[i]:
        num.append(0)
num.sort()
if num==arr:
    print("y")
else:
    print("n")