'''
a, b = map(int, input().split()) 입력받는건 같은데 케이스가 여러개라 while True:를 썻어야함

if a>b: 조건문에 a가 b보다 크면 다 되는줄 알았는데 생각해보니 a,b 가 0이라는거 생각했어야함
    print('Yes')
else:
    print('No')
'''
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')
        