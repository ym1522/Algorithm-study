import sys

s = ''
while True:
    s =  input() # sys.stdin.readline() : 개행문자까지 입력됨

    if s == '0':
        break
    
    s1 = s[:len(s)//2]
    
    if len(s) % 2 == 0: 
        s2 = s[:len(s)//2-1:-1]
    else: 
        s2 = s[:len(s)//2:-1]

    if s1 == s2:
        print('yes')
    else:
        print('no')
   