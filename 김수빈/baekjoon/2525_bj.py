import sys

cur_h, cur_m = map(int, sys.stdin.readline().split())
req_m = int(sys.stdin.readline())

m = cur_m + req_m
carry, m= m // 60, m % 60
h = (cur_h + carry) % 24

print(f"{h} {m}")