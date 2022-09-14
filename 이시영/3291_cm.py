from sys import stdin

botton=list(map(int,stdin.readline().split()))
hand=[]
for i in range(len(botton)):
    if botton[i]==2 and i==0:
        hand.append('L')
        continue
    if botton[i]==1:
        hand.append('L')
    elif botton[i]==3:
        hand.append('R')
    else:
        if hand[-1]=='L':
            hand.append('R')
        else:
            hand.append('L')
    
hand=' '.join(hand)
print(hand)