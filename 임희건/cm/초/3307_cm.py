# 개수 수열이란 초항이 1이고 길이가 1인 수열에서 만들어지는 수열이다.
# 개수 수열의 (i + 1)번째 항은 빈 수에서 시작하여 0부터 9까지 순서대로 보면서 i번째 항이 해당 숫자를 포함하고 있을 경우,
# 수의 오른쪽 끝에 해당 숫자와 해당 숫자가 나온 개수를 차례대로 추가하여 만들 수 있습니다.
# 예를 들어, K번째 항이 131이라면, 1이 2번, 3이 1번 등장하므로 K+1번째 항은 1231입니다.
# 개수 수열의 N번째 항을 출력하세요.

# 예제 입력1
# 4
# 예제 출력1
# 1121

# 예제 입력2
# 5
# 예제 출력2
# 1321

# 입력값 설명
# 정수 N 이 주어집니다. (1 ≤ N ≤ 20)

# 출력값 설명
# 초항이 1인 개수 수열의 N번째 항을 출력하세요.

# 풀이에 참고한 자료
# https://ponyozzang.tistory.com/703

import sys

N = int(sys.stdin.readline())    # N번째 입력
num = ['1']    # 초기 수열

# N번째 수열 생성
if N > 1:
    for i in range(2, N + 1):
        tmp = []

        for j in range(1, 21):
            if str(j) in num:
                tmp.append(str(j))
                tmp.append(str(num.count(str(j))))

        num = tmp.copy()

n = ''.join(num)

# 수열 출력
print(n)