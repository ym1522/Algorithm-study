import sys

ip = sys.stdin.readline().strip()
ip_split = ip.split(".")

print(ip_split)

if len(ip_split) > 1:
    print("IPv4")
else:
    print("IPv6")
