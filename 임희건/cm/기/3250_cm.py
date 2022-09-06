# 철수는 가수 A가 N일 후에 콘서트를 연다는 소식을 들었습니다.
# 철수는 가수 A를 몹시 좋아하기 때문에 반드시 이번 콘서트에 참여하고 싶습니다. 따라서 다른 일정이 콘서트와 겹치지 않도록 일찍부터 스케줄을 비워두려고 합니다.
# 오늘의 요일이 주어질 때, 콘서트 당일이 무슨 요일인지 구하는 프로그램을 작성해주세요.
# 단, 요일은 월요일부터 일요일까지 각각 MON, TUE, WED, THU, FRI, SAT, SUN으로 표현됩니다.

import sys

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

N = int(sys.stdin.readline())
day = sys.stdin.readline()

day = day[:-1]

for i in range(len(days)):
    if days[i] == day:
        N = N + i
        N = N % 7
        
        print(days[N])