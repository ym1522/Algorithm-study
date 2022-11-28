# lv2 - 최댓값과 최솟값
def solution(s):
    tmp = list(map(int, s.split(' ')))
    return str(min(tmp)) +' '+ str(max(tmp))
    
print(solution('-1 -1'))