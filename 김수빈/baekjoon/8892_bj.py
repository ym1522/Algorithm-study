import sys

def find_palin(k, words):
    for i in range(k):
        j = k - 1
        while i < j:
            word_1 = words[i] + words[j]
            word_2 = words[j] + words[i]
            if word_1 == word_1[::-1]:
                return word_1
            elif word_2 == word_2[::-1]:
                return word_2
            
            j -= 1
    return 0

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    words = []
    for _ in range(k):
        words += [sys.stdin.readline().strip()]
    print(find_palin(k, words))