import sys

a, b = map(int, sys.stdin.readline().split(' '))

if a <= b:
    x = abs(b - a)
    y = abs(a + (60-b))
else: 
    x = abs((60-a)+b)
    y = abs(a - b)
    
print(min(x, y))