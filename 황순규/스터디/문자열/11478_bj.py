import sys

S = sys.stdin.readline().strip()

strings = []
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        temp = S[i:j]
        strings.append(temp)
print(len(set(strings)))