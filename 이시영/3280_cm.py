from sys import stdin

n=int(stdin.readline())
dic={}
for i in range(n):
    a, b = map(str,stdin.readline().split())
    dic[a]=b
keys=input()
dic=list(dic.items())

flag=0
for i in range(len(dic)):
    if keys == dic[i][0]:
        print(dic[i][1])
        flag=1
        break
if flag==0:
    print(-1)