# level 1 - 폰켓몬
# 해시
from collections import Counter

# 폰켓몬의 종류가 가져갈 수 있는 수 보다 많으면 가져갈 수 있는 수를 리턴
# 폰켓몬의 종류가 가져갈 수 있는 수 보다 적으면 폰켓몬의 종류를 리턴
def solution(nums):
    n = len(nums) // 2
    mon = Counter(nums)     # 중복되는 값 제거 --> Counter import 안하고 set 써도 됨
    answer = n if len(mon) >= n else len(mon)       # min()으로 더 작은 값 찾으면 됨
    return answer