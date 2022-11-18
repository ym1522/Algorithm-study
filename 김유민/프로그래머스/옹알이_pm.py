def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    
    for tmp in possible:
        for i, baby in enumerate(babbling):
            if tmp in baby: 
                babbling[i] = baby.replace(tmp, '*')        # 옹알이 가능한 문자열이 존재하면 *로 대체
    
    for i, baby in enumerate(babbling):
        babbling[i] = baby.replace('*', '')                 # 위에서 대체했던 * 제거
    
    answer = babbling.count('')                             # 아무 값도 없는 원소이면 옹알이 가능이므로 count
    return answer