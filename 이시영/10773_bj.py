from sys import stdin

k=int(stdin.readline())
sta=[]
for _ in range(k):
    a=int(stdin.readline())
    if a==0:
        sta.pop()   # a가 0이면 sta의 맨 뒤 원소 삭제
    else:
        sta.append(a) 
    
print(sum(sta))