'''
n = int(input()) 입력이 두개라 처음에 이렇게 했는데 
m = int(input()) 찾아보니 map이랑 split써서 푸는거였다

print(n//m)
print(n%m)
'''
n, m = map(int, input().split())

print(n//m)
print(n%m)