s = list(input().lower())
a = list(set(s))

max = 0
max_a = ''
for i in a:
    if max < s.count(i):
        max = s.count(i)
        max_a = i
    elif max == s.count(i):
        max_a = '?'
print(max_a)