'''
2x2 -> 3
1x1 -> 0

1x1 이 1개 조각
NxM 크기의 초콜릿 = NxM 개의 초콜릿 조각.

결국은 초콜릿 조각이 1개 남을때까지 1x1씩 처리
'''

N, M = map(int, input().split())

print((N*M) - 1)