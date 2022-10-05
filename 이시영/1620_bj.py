from sys import stdin

n, m = map(int, stdin.readline().split())
s = dict()

for i in range(1,n+1):
    po = stdin.readline().rstrip()
    s[i]=po
    s[po]=i

for i in range(m):
    ch = stdin.readline().rstrip()
    if ch.isdigit():
        print(s[int(ch)])
    else:
        print(s[ch])