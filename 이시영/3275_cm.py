from sys import stdin
n=list(stdin.readline())
for i in range(len(n)):
    if n[i]=='\'':
        n[i]=('\\\'')
    elif n[i]=='\"':
        n[i]=('\\\"')
    elif n[i]=='\\':
        n[i]=('\\\\')
n="".join(n)
n=n.strip()  # \n을 없앰. \n이 있는거 때문에 고생많이 함...
print(n)