# 가영이와 친구들이 패밀리 레스토랑에 왔습니다. 계산은 더치페이를 하기로 했습니다. 
# 음식별로 해당 음식의 가격과 누가 그 음식을 먹었는지 리스트가 주어집니다. 해당 음식을 먹은 사람들은 그 음식에 대해선 1/n 방식으로 금액을 지불합니다. 
# 가영이와 친구들이 먹은 모든 음식에 대해서 가격과 리스트가 주어질 때, 각자 얼마를 내야 하는지 계산하는 프로그램을 작성해주세요.

# 예제 입력1
# 5 3
# 3000 3
# 1 2 3
# 5000 2
# 4 5
# 10000 5
# 1 2 3 4 5
# 예제 출력1
# 3000 3000 3000 4500 4500

# 예제 입력2
# 5 1
# 100000 1
# 3
# 예제 출력2
# 0 0 100000 0 0

# 입력값 설명
# 첫째 줄에 레스토랑에 간 인원 수 N과 주문한 음식 수 M이 주어집니다. (1 ≤ N, M ≤ 500)
# 그 다음 줄부터 각 음식에 대하여 2개의 줄, 총 2M개의 줄이 입력됩니다.
# 첫 번째 줄에는 음식의 가격 C와 해당 음식을 먹은 사람 수 n이 주어집니다. (n ≤ C ≤ 10,000,000) C는 n으로 나누어 떨어짐이 보장됩니다.
# 두 번째 줄에는 자연수 n개가 공백으로 구분되어 주어집니다. 각 i는 해당 음식을 먹은 사람을 의미하고 서로 중복되지 않습니다. (1 ≤ i ≤ N)

# 출력값 설명
# N개의 정수를 공백으로 구분하여 출력합니다. i번째 정수는 i번째 사람이 내야 할 금액을 의미합니다.