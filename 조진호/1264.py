
list = ['a','e','i','o','u']
while True:
    s = input()
    if s == "#":
        break
    
    count=0
    for i in s:
        if i.lower() in list:
            count += 1
    print(count)
"""
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
    """