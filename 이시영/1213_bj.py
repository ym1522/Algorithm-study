from sys import stdin

name=list(input())
count=[0 for _ in range(26)]
for i in name:
    count[ord(i)-65]+=1

cnt=0
center=""
left=""
for i in range(26):
    if count[i]%2 == 1:
        cnt += 1
        center += chr(i+65)
    left+=chr(i+65)*(count[i]//2)
if cnt>1:
    print("I'm Sorry Hansoo")
else:
    print(left+center+left[::-1])