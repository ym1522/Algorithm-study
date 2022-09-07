import sys

directions = list(sys.stdin.readline().split())
D = {'1' : 'L', '3' : 'R'}
stack = []
for dir in directions:
    if dir in D: stack += [D[dir]]
    elif not stack : stack += ['L']
    else: stack += ['R' if stack[-1] == 'L' else 'L']
print(' '.join(stack))