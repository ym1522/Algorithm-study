S = input().strip()

answer = []
for i in range(ord('a'), ord('a') + 26):
    answer += [str(S.count(chr(i)))]
print(' '.join(answer))