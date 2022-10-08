import sys

h, m = map(int, sys.stdin.readline().split())
t = int(input())
# 더한 거에 60으로 나눈 몫 만큼 시간이 증가, 하지만 24시에 도달하면 0시가 되므로 24로 나눠 나머지만 계산
h = (h + ((m + t)//60)) % 24 
# 분은 그냥 60 나눠준거의 나머지 계산만 하면 됨
m = (m + t)%60 
print(h, m)