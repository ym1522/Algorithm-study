arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    s = input()
    count = 0
    if s == '#':
        break
    for i in range(len(s)):
        if s[i] in arr:
            count += 1
    print(count)