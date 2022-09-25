import sys

n = int(sys.stdin.readline())
words = []
res = []
l = []

for i in range(n):
    words.append(sys.stdin.readline().rstrip())
for w in words:
    l.append(len(w))
words = list(set(words))
l = list(set(l))

l.sort()
words.sort()

for i in l:
    for w in words:
        if len(w) == i:
            res.append(w)
for r in res:
    print(r)


# 람다식으로 짧게 풀이 가능 ㅠㅠ