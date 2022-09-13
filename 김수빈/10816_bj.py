import sys

def search_binary(cards, tgt, i, j):
    if i == j: return i if cards[i] == tgt else -1

    mid = (i + j) // 2
    if cards[mid] == tgt:
        return mid
    elif cards[mid] > tgt:
        return search_binary(cards, tgt, i, mid)
    else:
        return search_binary(cards, tgt, mid + 1, j)

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
D = {}
for c in cards:
    if not c in D: D[c] = 1
    else: D[c] += 1
cards = list(set(cards))
cards.sort()

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for n in nums:
    idx = search_binary(cards, n, 0, len(cards) - 1)
    if idx < 0: print("0", end=' ')
    else:
        print(D[cards[idx]], end=' ')