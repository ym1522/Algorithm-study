import sys, math

a, b, v = map(int, sys.stdin.readline().split())
day, m = 0, 0

#---------반복문 안됨---------#
# while True:
#     m += a
#     day += 1
    
#     if m >= v: break
#     else: m -= b
# print(day)

res = -(a-v)/(a-b) +1
print(math.ceil(res))   # 올림해줘야함.