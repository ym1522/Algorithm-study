import sys
input = sys.stdin.readline

a,b,c,m = map(int, input().split())

# 일의양
work = 0

# 피로도
rest = 0

for i in range(24):
    if rest + a > m:
        #쉬는 타임
        rest -= c
        if rest < 0:
            rest = 0
    else:
        work += b
        rest += a
        
print(work)