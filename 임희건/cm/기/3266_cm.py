# 우리가 사용하는 도로명 주소의 건물번호는 다음과 같은 규칙으로 부여됩니다. 
# 1. 건물번호는 도로 시작점에서 20m 간격으로 부여됩니다.
# 2. 건물번호 표기는 도로방향을 기준으로 왼쪽에 홀수, 오른쪽에 짝수를 부여합니다. 
# 어떤 건물의 건물번호가 주어졌을 때 이 건물이 도로방향을 기준으로 왼쪽에 있는지 오른쪽에 있는지 판단하는 프로그램을 작성해주세요.

import sys

T = int(sys.stdin.readline())
building = []

for i in range(T):
    building.append(int(sys.stdin.readline()))
    
for j in building:
    if j % 2 == 1:
        print('L')
        
    else:
        print('R')