import sys

S = sys.stdin.readline().strip()
strings = []

for i in range(len(S)):
    strings.append(S[i:])

strings.sort()

for i in strings:
    print(i)