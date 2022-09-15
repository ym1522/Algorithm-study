import sys
N, M = map(int, sys.stdin.readline().split())
snake = sys.stdin.readline().strip()
orders = sys.stdin.readline().strip()

D = {
    'r':{
        'R' : 'b', 'L' : 't', 'F' : 'r',
    },
    'l':{
        'R' : 't', 'L' : 'b', 'F' : 'l',
    },
    't':{
        'R' : 'r', 'L' : 'l', 'F' : 't',
    },
    'b':{
        'R' : 'l', 'L' : 'r', 'F' : 'b',
    },
}
stack = [(0, i) for i in range(-N + 1, 1)]
cur = 'r'
for order in orders:
    cur = D[cur][order]
    if cur == 'b':
        x, y = stack[-1][0] + 1, stack[-1][1]
    if cur == 't':
        x, y = stack[-1][0] - 1, stack[-1][1]
    if cur == 'r':
        x, y = stack[-1][0], stack[-1][1] + 1
    if cur == 'l':
        x, y = stack[-1][0], stack[-1][1] - 1
    stack += [(x, y)]
answer = list(map(lambda x: (x[1][0], x[1][1], x[0]), zip(snake, stack[::-1][:N])))
answer.sort()
print(''.join(list(map(lambda x: x[-1], answer))))