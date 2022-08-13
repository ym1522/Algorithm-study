#case1) 입력 string

n = input()

m = n

#출력 변수
cnt = 0

# 정답과 같을때 까지 반복
while True:
    
    # 10보다 작은 경우 두 자리 수 만들기.
    if int(m) < 10:
        m = "0" + m
        
    # 2) 각 자리 더하기 
    sum_value = int(m[0]) + int(m[-1]) 
    
    # 3) 새로운 수 만들기
    m = str(m[-1]) + str(sum_value)[-1]
    
    cnt += 1
    
    # ex) '9' == '09'
    if int(n) == int(m):
        break

print(cnt)


#case 2) 입력 int - 나누기와 나머지 연산으로 접근가능.