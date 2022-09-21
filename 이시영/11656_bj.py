from sys import stdin

s = stdin.readline().rstrip()

a =[]
for i in range(len(s)):
    a.append(s[i:])
a=sorted(a)
for i in range(len(a)):
    print(a[i])