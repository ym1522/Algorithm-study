from sys import stdin

n=list(stdin.readline().rstrip())
cl=0
for i in n:
    if i=='3' or i=='6' or i=='9':
        cl+=1
if cl==0:
    n="".join(n)
    print(n)
else:
    print("clap"*cl)