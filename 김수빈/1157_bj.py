word = input().strip().lower()
counts = [(word.count(c), c) for c in set(word)]
counts = sorted(counts, key=lambda x: x[0], reverse=True)
if len(counts) == 1: print(counts[0][-1].upper())
else:
    if counts[1][0] == counts[0][0]: print("?")
    else:
        print(counts[0][-1].upper())