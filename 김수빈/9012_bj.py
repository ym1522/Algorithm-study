import sys

def solution(string):
    stack = []
    for s in string:
        if s == '(':
            stack += [s]
        else:
            if not stack: return False
            stack.pop()
    
    return len(stack) == 0

N = int(sys.stdin.readline())
strings = list(map(lambda x: x.strip(), sys.stdin.readlines()))

for string in strings:
    if not solution(string): print("NO")
    else: print("YES")