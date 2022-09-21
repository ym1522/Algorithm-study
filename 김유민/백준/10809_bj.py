import sys

a = [-1] * 26

string = sys.stdin.readline().rstrip()
for i, s in enumerate(string):
    if a[ord(s)-97] != -1: pass
    else: a[ord(s)-97] = i

for i in a:
    print(i, end=' ')