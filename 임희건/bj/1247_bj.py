import sys

S = []

for i in range(3):
    add = int(sys.stdin.readline())
    sum = 0
    
    for j in range(add):
        sum = sum + int(sys.stdin.readline())
        
    if sum > 0:
        S.append('+')
        
    elif sum < 0:
        S.append('-')
        
    else:
        S.append('0')
        
for k in S:
    print(k)