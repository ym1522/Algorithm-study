import sys
N, M = map(int, sys.stdin.readline().split())
names = list(map(lambda x: x.strip(), sys.stdin.readlines()))

no_hear = names[:N]
no_see = names[N:]

answer = list(set(no_hear).intersection(set(no_see)))
answer.sort()
print(len(answer))
print('\n'.join(answer))