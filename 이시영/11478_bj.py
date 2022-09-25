from sys import stdin

s = stdin.readline().rstrip()
ch=set()
for i in range(len(s)):
    for j in range(i,len(s)):
        ch.add(s[i:j+1])
print(len(ch))