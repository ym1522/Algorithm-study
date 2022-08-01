print('1부터 n까지 합')
n = int(input('n을 입력하시오 : '))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
    
print(f'1부터 n까지 합은 {sum} 입니다.')