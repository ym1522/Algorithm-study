import sys
# string의 특성을 활용하여 플기
n = tmp = int(sys.stdin.readline())
cnt = 0

while True:
    num1 = n // 10
    num2 = n % 10
    res = num1 + num2
    cnt += 1
    n = int(str(n % 10) + str(res % 10))
    if tmp == n:
        break

print(cnt)
