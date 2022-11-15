# lv2 - 다음 큰 숫자
def solution(n):
    answer = 0
    N = str(bin(n)[2:])
    
    while True:
        n += 1
        tmp = str(bin(n)[2:])
        if tmp.count('1') == N.count('1'):
            answer = n
            break
    
    return answer