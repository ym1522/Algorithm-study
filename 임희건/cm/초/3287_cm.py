# 철수는 1번부터 N번까지의 물건을 각각 하나씩 구매하려고 합니다. 돈이 충분하지 않아 한번에 모든 물건을 구매할 수는 없습니다. 따라서 철수는 적절한 순서로 물건을 구매하려고 합니다.
# 철수가 물건을 구매하는 순서는 다음과 같습니다.
# 1) 우선순위가 가장 높은 물건을 먼저 구매합니다.
# 2) 우선순위가 같은 물건이 여러개이면 가격이 싼 물건을 먼저 구입합니다.
# 3) 우선순위와 가격이 모두 같은 물건이 여러개이면 해당 물건을 판매하는 가게까지의 거리가 작은 물건을 먼저 구매합니다.
# 물건들의 정보가 주어졌을 때, 철수가 물건 구매 순서를 알려주는 프로그램을 작성해주세요.
# 단, 서로 다른 두 물건의 우선순위, 가격, 판매하는 가게까지의 거리가 모두 같은 경우는 존재하지 않습니다.

# 예제 입력1
# 5
# 5 1 3
# 5 1 4
# 5 1 2
# 5 2 1
# 5 2 4
# 예제 출력1
# 3 1 2 4 5

# 예제 입력2
# 3
# 1 5 3
# 3 1 5
# 5 1 3
# 예제 출력2
# 3 2 1

# 입력값 설명
# 첫째 줄에 물건의 개수를 의미하는 양의 정수 N이 주어집니다. (1 ≤ N ≤ 10)
# 이어서 N개의 줄에 걸쳐 i(1 ≤ i ≤ N)번 물건의 정보를 의미하는 3개의 양의 정수 a, b, c가 공백으로 구분되어 주어집니다. a, b, c는 각각 물건의 우선순위, 가격, 판매하는 가게까지의 거리를 의미합니다. (1 ≤ a, b, c ≤ 100)

# 출력값 설명
# 첫째 줄에 물건의 번호를 철수가 구매하는 순서대로, 공백으로 구분하여 출력합니다.