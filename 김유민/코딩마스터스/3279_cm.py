import sys

ip = sys.stdin.readline()
if ':' in ip:
    print("IPv6")
else:
    print("IPv4")