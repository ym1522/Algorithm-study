a = ['a','e','i','o','u']

while True:
    s = input().lower()
    
    if s == '#':
        break
    cnt = 0
    for i in a:
        cnt += s.count(i)
        
    print(cnt)