import sys

def solution(N, M, cards):
    cards.sort()
    i, j, k = N - 3, N - 2, N - 1
    answer = None
    for i in range(N - 3, -1, -1):
        j = i + 1
        k = N - 1
        while j < k:
            sum_val = cards[i] + cards[j] + cards[k]
            if sum_val > M:
                k -= 1
            elif sum_val == M: return M
            else:
                answer = sum_val if answer is None or M - sum_val < M - answer else answer
                j += 1
    return answer

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
print(solution(N, M, cards))