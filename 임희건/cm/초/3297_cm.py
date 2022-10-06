# 게임 등을 만들 때, 두 개체가 충돌했는지 판별하는 방법은 여러가지입니다.
# 직관적으로 생각나는 방법은 화면에 출력되는 이미지가 실제로 맞닿았는지 판별하는 것입니다.
# 하지만 이런 충돌 판정은 이미지의 윤곽이 복잡할수록 훨씬 큰 비용이 듭니다. 만약 실시간 온라인 격투 게임에서 이런 판정 방식을 사용하면 어떻게 될까요?
# 복잡한 충돌 판정으로 인해 서버에 비용이 쌓이고, 사용자에게 '딜레이'가 발생하는 불상사가 발생하게 됩니다.
# 비용이 큰 위 방법 대신, 충돌 마스크를 사용할 수 있습니다. 충돌 마스크란 화면에 출력되는 이미지 대신 충돌 판정을 수행하는 보이지 않는 다각형입니다.
# 여러분은 가장 간단한 다각형인 정사각형을 충돌 마스크로 사용해보려 합니다. 각각 서로 다른 두 개체의 충돌 마스크에 해당하는 두 정사각형의 정보가 주어집니다.
# 두 정사각형이 모두 네 변이 x축 또는 y축과 평행할 때, 두 정사각형이 서로 접하거나 겹쳐 있는지 판정해주세요.

# 예제 입력1
# 3 3 10
# 50 50 8
# 예제 출력1
# NO

# 예제 입력2
# 1 1 1
# 2 2 1
# 예제 출력2
# YES

# 입력값 설명
# 첫 번째 줄에 첫 번째 정사각형의 중점 x1, y1 과 변의 길이 r1가 공백을 구분으로 주어집니다.
# 두 번째 줄에 두 번째 정사각형의 중점 x2, y2 과 변의 길이 r2가 공백을 구분으로 주어집니다.
# (1 ≤ x1, y1, x2, y2, r1, r2 ≤ 1,000)

# 출력값 설명
# 두 정사각형이 접하거나 겹쳐있으면 "YES", 아니면 "NO"를 출력합니다.

import sys

x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())

rec_x1 = x1 - r1 / 2
rec_y1 = y1 - r1 / 2
rec_x2 = x1 + r1 / 2
rec_y2 = y1 + r1 / 2

rec2_x1 = x2 - r2 / 2
rec2_y1 = y2 - r2 / 2
rec2_x2 = x2 + r2 / 2
rec2_y2 = y2 + r2 / 2

min_rec_x = min(rec_x1, rec_x2)
min_rec_y = min(rec_y1, rec_y2)
max_rec_x = max(rec_x1, rec_x2)
max_rec_y = max(rec_y1, rec_y2)

if not min_rec_x <= rec2_x1 <= max_rec_x and not min_rec_x <= rec2_x2 <= max_rec_x and not min_rec_y <= rec2_y1 <= max_rec_y and not min_rec_y <= rec2_y2 <= max_rec_y:
    print("NO")

else:
    print("YES")