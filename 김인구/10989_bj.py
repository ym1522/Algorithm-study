'''
리스트에 값 다 받아서 정렬처리 하면 메모리 초과
입력받는 수의 개수 : 최대 10,000,000 = 10**7 = 10MB  조건은 8MB
수의 최대 값 : 10,000 이하.

최대값이 여러번 나와도 상관없으니깐
ans = [0] * 10001 로 해서 각 위치에 +1 넣고 낮은 인덱스부터 값 출력
'''
import sys

input = sys.stdin.readline

n = int(input())
ans = [0] * 10001 # 10,000번째값도 필요

for _ in range(n):
    ans[int(input())] += 1
    
for idx in range(10001):
    for k in range(ans[idx]):
        print(idx)

    