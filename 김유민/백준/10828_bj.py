import sys

n = int(sys.stdin.readline())
MyStack = []

for i in range(n):
    s = sys.stdin.readline().rstrip().split()
    
    if s[0] == 'push': MyStack.append(int(s[1]))
    if s[0] == 'pop': 
        try: print(MyStack.pop())
        except IndexError: print(-1)
    if s[0] == 'size': print(len(MyStack))
    if s[0] == 'empty': print(1 if len(MyStack)==0 else 0)
    if s[0] == 'top': 
        try: print(MyStack[-1])
        except IndexError: print(-1)