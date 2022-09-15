import sys

A = sys.stdin.readline().strip()
if len(A.split('.')) == 4:
    print("IPv4")
else:
    print("IPv6")