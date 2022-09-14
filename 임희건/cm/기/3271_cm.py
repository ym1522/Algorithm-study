# 가영이와 친구들은 2주만에 코딩 연습 문제 100문제를 만들어야 합니다. 
# 2주차 수요일, 가영이는 자기 자신과 친구들이 각각 몇 문제를 만들었는지 조사했습니다. 
# 각 친구들이 만든 문제의 개수가 주어질 때, 앞으로 몇 문제를 더 만들어야 하는지 알아내는 프로그램을 작성해주세요.
# 만든 문제가 100문제 이상이라면, 문제를 더 만들 필요가 없습니다.

import sys

last = 100

N = sys.stdin.readline()
quiz = sys.stdin.readline().split()

for i in quiz:
    last = last - int(i)
    
if last < 0:
    last = 0

print(last)