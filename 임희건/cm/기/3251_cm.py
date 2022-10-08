# 철수는 방학 때 자격증 시험에 응시했습니다.
# 철수가 응시한 자격증 시험은 총 5개의 과목으로 구성되고, 자격증을 취득하려면 모든 과목에서 40점 이상, 전과목 평균 60점 이상 득점해야 합니다.
# 철수의 시험 점수가 주어졌을 때, 철수의 자격증 취득 여부를 구하는 프로그램을 작성해주세요.

import sys

result = True

score = list(map(int,sys.stdin.readline().split()))

for i in score:
    if i < 40:
        result = False

    if sum(score) / 5 < 60:
        result = False

if result:
    print('P')

else:
    print('F')