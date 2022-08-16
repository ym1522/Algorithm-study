import sys
from bisect import bisect_left

def solution(cards, cands):
    if not cands: return []
    if not cards: ['0' * len(cands)]
    if len(cands) == 1:
        return ['1'] if cands[0][1] in cards else ['0']

    mid_cands = len(cands) // 2
    try:
        mid_cards = cards.index(cands[mid_cands])
    except:
        mid_cards = bisect_left(cards, cands[mid_cands][1])

    left = solution(cards[:mid_cards], cands[:mid_cands])
    right = solution(cards[mid_cards:], cands[mid_cands:])
    return left + right

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(sys.stdin.readline())
cands = list(map(int, sys.stdin.readline().split()))
cands = sorted(enumerate(cands), key=lambda x: x[-1])
indices = list(map(lambda x: x[0], cands))


answer = solution(cards, cands)
answer = sorted(list(zip(indices, answer)), key=lambda x: x[0])
print(' '.join(list(map(lambda x: x[1], answer))))