import sys

count = 0

N = int(sys.stdin.readline())
n = N

while True:
    a = n//10
    b = n%10
    c = a+b
    n = (b*10) + (c%10)
    count += 1
    
    if N == n: break

print(count)