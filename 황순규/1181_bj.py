import sys

N = int(sys.stdin.readline())

words = {}

for i in range(N):
    w = sys.stdin.readline().strip()
    
    if len(w) not in words.keys():
        words[len(w)] = [w]
    else:
        if w not in words[len(w)]:
            words[len(w)].append(w)

words = sorted(words.items())

for i in words:
    i[1].sort()
    
for i in words:
    for j in i[1]:
        print(j)