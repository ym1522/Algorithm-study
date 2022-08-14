# 정답 맞았는데 출력 형식이 아니라고 나옴
a = int(input())
for i in range(0,a+1):
    print(" "*(a-i) +"*"*i)