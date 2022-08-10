from sys import stdin
IP=stdin.readline()
if '.' in IP:
    print("IPv4")
else:
    print("IPv6")