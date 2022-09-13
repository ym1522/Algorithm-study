import sys

money = int(sys.stdin.readline())
money = 1000 - money
cnt = 0

for m in [500, 100, 50, 10, 5, 1]:
    cnt += money // m
    money %= m
    
print(cnt)    