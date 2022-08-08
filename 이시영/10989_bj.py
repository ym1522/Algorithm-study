from sys import stdin
n= int(stdin.readline())
m=[0]*10001
for _ in range(n):
    cnt= int(stdin.readline())
    m[cnt] +=1

for i in range(10001):
    if m[i]:
        for j in range(m[i]):
            print(i)