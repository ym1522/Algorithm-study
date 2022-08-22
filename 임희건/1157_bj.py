import sys

word = sys.stdin.readline().upper()
word = word[:-1]
word_short = list(set(word))
count = []

for i in word_short:
    c = word.count(i)
    count.append(c)

if count.count(max(count)) > 1:
    print('?')

else:
    print(word_short[count.index(max(count))])