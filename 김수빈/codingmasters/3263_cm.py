import sys
vol, cal = map(int, sys.stdin.readline().split())
print("YES") if cal / vol <= 0.04 else print("NO")