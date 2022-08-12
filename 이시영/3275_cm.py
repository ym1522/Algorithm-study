from sys import stdin
n=list(stdin.readline().rstrip())  # .rstrip() \n을 없애줌
for i in range(len(n)):
    if n[i]=='\'':
        n[i]=('\\\'')
    elif n[i]=='\"':
        n[i]=('\\\"')
    elif n[i]=='\\':
        n[i]=('\\\\')
n="".join(n)
print(n)