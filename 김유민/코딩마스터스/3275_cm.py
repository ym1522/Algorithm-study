import sys

s = sys.stdin.readline()
ans = []

for i in s:
    if i == "'" or i == '"' or i == '\\':
        ans.append("\\")
    ans.append(i)

for i in ans:
    print(i, end='')