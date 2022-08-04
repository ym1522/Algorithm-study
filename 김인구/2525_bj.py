a, b = map(int, input().split())
c = int(input())

flag = 0

m = b+c
flag = m // 60
m = m % 60

h = a + flag
h = h % 24

print(h, m)    
