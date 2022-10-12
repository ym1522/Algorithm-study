# 1920 - 수 찾기
# 메모리: 46800KB, 시간:712ms

import sys

# --- 시도 1: 시간 초과 ---
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))

# for i in m_list:
#     check = 0
#     if i in a: check = 1
#     print(check)


# --- 시도 2: 시간 초과---
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))

# check = [1 if i in a else 0 for i in m_list]
# print(*check, sep='\n')


# --- 시도 3: 성공---
# 이분 탐색 알고리즘
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target, left, right):
    if left > right: return 0
    mid = (left + right) // 2
    if target == arr[mid]: return 1
    elif target > arr[mid]: return binary_search(arr, target, mid+1, right)  # 재귀함수 호출 시 return !!!
    elif target < arr[mid]: return binary_search(arr, target, left, mid-1)
    # 부등호 방향 주의

a.sort()
for i in m_list:
    print(binary_search(a, i, 0, n-1))
    
'''
--- in 연산자의 시간 복잡도 ---
* 자료형 마다 시간 복잡도가 다름
  - list, tuple: O(n) - 전부 순회
  - set, dictionary: O(1), 최악의 경우 O(n) - 내부에서 해시를 통해 저장하므로 접근 시간은 O(1)이지만 해시 충돌이 일어날 경우 O(n)
  
실패한 코드에서는 in list를 사용하였기 때문에 리스트의 모든 원소를 방문 => 시간 초과
이분 탐색은 대상의 절반씩 줄여나가며 target을 찾기 때문에 빠르게 연산할 수 있음 => O(logN)의 시간 복잡도
'''