import sys

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    lands = []
    for i in range(h):
        line = map*(int, sys.stdin.readline().split())
        lands.append(line)
        
        ### 못풂