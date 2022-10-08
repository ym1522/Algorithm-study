# 자동차 번호판은 4자리의 숫자로 이루어져 있습니다.
# 치훈이는 길을 걸어가다가 자동차 번호판을 보면, 번호판에 적힌 4개의 숫자로 등식을 만들 수 있는지 생각하는 것을 좋아합니다.
# 자동차 번호판에 적인 4개의 숫자 ABCD가 주어졌을 때, 2개의 덧셈기호와 등호를 이용하여 A+B=C+D꼴의 등식을 만들 수 있는지 알려주는 프로그램을 작성해주세요.
# 단, A, B, C, D는 입력으로 주어진 순서가 아니어도 됩니다.
# 예를 들어 번호판의 숫자가 3142라면, 3+2=1+4 라는 등식을 만들 수 있습니다.

# 예제 입력1
# 3142
# 예제 출력1
# YES

# 예제 입력2
# 9023
# 예제 출력2
# NO

# 입력값 설명
# 4자리 숫자가 연속되어 주어집니다.

# 출력값 설명
# 등식을 만들 수 있으면 YES, 없으면 NO를 출력합니다.

import sys

N = int(sys.stdin.readline())    # 번호판 숫자
n = []    # 번호 한자리씩 저장
check = False    # 등식 가능 여부

# 번호 한자리씩 저장
for _ in range(4):
    tmp = N % 10
    n.append(tmp)
    N = N // 10

# 등식 가능 여부 판단
num = sum(n) / 2

if num % 1 == 0:
    for i in range(3):
        for j in range(i + 1, 4):
            if int(num) == n[i] + n[j]:
                n_tmp = n.copy()
                del n_tmp[j]
                del n_tmp[i]

                if int(num) == sum(n_tmp):
                    check = True

# 등식 가능 여부 출력
if check:
    print('YES')

else:
    print('NO')