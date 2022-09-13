import sys
shirt, pants = map(int, sys.stdin.readline().split())
hanger, p_hanger = map(int, sys.stdin.readline().split())

print("YES") if max(0, pants - p_hanger) + shirt <= hanger else print("NO") 