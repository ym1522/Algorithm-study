from sys import stdin

a,b,c,d=map(str,stdin.readline().split())

if int(a)==0:
    print(0)
else:
    if d=='Private':
        if int(a)==5 or int(a)==6:
            print(20)
        elif c=='N' and (b=="ROKA" or b=='ROKN'):
            print(32)
        else:
            print(28)
    else:
        print(28)