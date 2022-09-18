import sys

N, M = map(int, sys.stdin.readline().split())
spotters = list(map(int, sys.stdin.readline().split()))[1:]
parties = []
for p in range(M):
    parties += [list(map(int, input().split()))[1:]]

attending = [1] * M
stack = [spotters]
while stack:
    spot = stack.pop()
    for i in range(M): 
        if set(parties[i]).intersection(set(spot)) and attending[i] == 1:
            attending[i] = 0
            stack += [parties[i]]
print(attending.count(1))