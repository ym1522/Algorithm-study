from sys import stdin
from collections import deque  # deque 사용
n=int(stdin.readline())
q=deque([i for i in range(1,n+1)])  # 1~ n개 까지의 deque 생성

while len(q)!=1:
    q.popleft()   # q의 맨앞의 원소를 삭제
    q.append(q.popleft()) # q의 맨 앞의 원소를 q의 맨 뒤로 보냄
print(q[0])