# 키패드 누르기

def solution(numbers, hand):    
    answer = ''
    cur_L, cur_R = 10, 12
    for i in numbers:
        if i == 0: i = 11
        if i in [1, 4, 7]:
            answer += 'L'
            cur_L = i
        elif i in [3, 6, 9]:
            answer += 'R'
            cur_R = i
        else:
            dist_L = abs((i - 1)%3 - (cur_L - 1)%3) + abs((i - 1)//3 - (cur_L - 1)//3)
            dist_R = abs((i - 1)%3 - (cur_R - 1)%3) + abs((i - 1)//3 - (cur_R - 1)//3)
            if dist_L < dist_R:
                answer += 'L'
                cur_L = i
            elif dist_L > dist_R:
                answer += 'R'
                cur_R = i
            else:
                if hand == "right":
                    answer += 'R'
                    cur_R = i
                else:
                    answer += 'L'
                    cur_L = i
    return answer