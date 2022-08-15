t = int(input())

for tc in range(t):
    floor = int(input()) #층
    room = int(input()) #호
    
    # n번방에는 n명씩 존재
    result = [r for r in range(room+1)]
    
    for f in range(floor): #n층 까지
        for r in range(1, room+1): # 현재방은 이전방의 합
            result[r] += result[r-1]

    print(result[room])