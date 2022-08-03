chess_board = []    # 체스판 색상
chess = []          # 말 위치
answer = 0          # 말이 있는 흰색 칸 개수

# 체스판 색상 설정
for j in range(0, 8):
    line_board = []
    
    for k in range(0, 8):
        if j % 2 == 0:
            if k % 2 == 0:
                line_board.append(0)
                
            else:
                line_board.append(1)
        
        else:
            if k % 2 == 0:
                line_board.append(1)
                
            else:
                line_board.append(0)
            
    chess_board.append(line_board)

# 말 위치 입력    
for i in range(0, 8):
    line = input()
    chess.append(str(line))

# 말이 있는 흰색 칸 개수 확인
for l in range(0, 8):
    for m in range(0, 8):
        if chess[l][m] == 'F' and chess_board[l][m] == 0:
            answer += 1

print(answer)
