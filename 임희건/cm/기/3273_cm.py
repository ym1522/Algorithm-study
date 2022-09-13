# 우박수열 a는 모든 자연수 i에 대하여 다음과 같이 정의되는 수열입니다.
# a_(i+1) = a_i/2 (a_i가 짝수인 경우)
#  = 3*a_i+1 (a_i가 홀수인 경우)
# 로타르 콜라츠(Lothar Collatz)는 초항이 자연수인 모든 우박수열 a에 대하여, a_i = 1이 되게 하는 i가 존재할 것이라는 추측을 하였고, 초항이 10,000 이하인 우박수열에 대해서는 이 추측이 참이라고 증명되어 있습니다.
# 어떤 우박수열의 초항 N이 주어집니다. 이 우박수열의 항이 처음으로 1이 될 때까지 출력해주세요.

import sys

num = []

N = int(sys.stdin.readline())

if N == 1:
    print(N)
    
else:
    num.append(N)
    
    while N != 1:
        if N % 2 == 0:
            N = int(N / 2)
            
        else:
            N = 3 * N + 1
            
        num.append(N)
        
    print(*num)