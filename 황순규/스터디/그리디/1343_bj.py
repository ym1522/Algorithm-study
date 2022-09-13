import sys

S = sys.stdin.readline().strip()

S_list = S.split('.')
board = ''
flag = True

for i in S_list:
    length = len(i)
    
    if length % 2 == 0:
        
        while length > 0:
            if length >= 4:
                board += 'AAAA'
                length -= 4
            else:
                board += 'BB'
                length -= 2
        board += '.'
    else:
        flag = False
        break
    
if flag:
    print(board[:-1])
else:
    print(-1)