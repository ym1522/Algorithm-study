from sys import stdin
a=list(stdin.readline().strip())

if len(a)==5:
    print("".join(a))
else:
    for i in range(0,5-len(a)):
        a.insert(i,'0')
    print("".join(a))