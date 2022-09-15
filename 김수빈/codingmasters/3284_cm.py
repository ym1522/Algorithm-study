import sys

N = int(sys.stdin.readline())
cards = list(map(lambda x: x.strip(), sys.stdin.readlines()))
deq = ['0']
for i, c in enumerate(cards):
    if c == 'U': deq += [str(i + 1)]
    else: deq = [str(i + 1)] + deq
print(' '.join(deq))