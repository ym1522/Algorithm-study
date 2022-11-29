# 2684 - 동전 게임
# 메모리: 30840KB, 시간: 68ms

import sys

# coin_res = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}  --- 틀림
# 새로운 테스트 케이스마다 dictionary를 초기화하지 않아서 생긴 문제 !

p = int(sys.stdin.readline())

for i in range(p):
    coin_res = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}  # for문이 돌 때마다 dictionary 선언
    coin = sys.stdin.readline().rstrip()
    
    for j in range(38):
        coin_res[coin[j:j+3]] += 1
        
    res = list(coin_res.values())
    print(*res)