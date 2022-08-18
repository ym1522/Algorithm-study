import sys

h, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

m += t
if m >= 60:
    h += m//60
    m %= 60
    if h > 23:
        h -= 24
        
print(h, m)