import sys

s = sys.stdin.readline().rstrip()
res = []
for i in s:
    if ord(i) < 91:
        res.append(ord(i)+32)
    else: res.append(ord(i)-32)

for i in res:
    print(chr(i), end='')