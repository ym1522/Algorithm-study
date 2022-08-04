
while True:
    n = input()
    
    ans = 0
    
    if n == '#':
        break
    
    for c in n:
        if 'a' == c or 'e' == c or 'i' == c or 'o' == c or 'u' == c:
            ans += 1
        elif 'A' == c or 'E' == c or 'I' == c or 'O' == c or 'U' == c:
            ans += 1
    print(ans)