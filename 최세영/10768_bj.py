# 만약 날짜가 2월 18일 전이면, "Before"을 출력한다.
# 만약 날짜가 2월 18일 후면, "After"을 출력한다.
# 만약 2월 18일이라면 "Special" 을 출력한다.
'''
if a == 2 and b == 18:
    print('Special')
elif a >=2 and b>18: 3월1일같은경우 조건이 안댐 그래서 다시 처음부터 조건
    print('After')
else:
    print('Before')
'''

a = int(input())
b = int(input())
result = ""
if a < 2:
    result = "Before"
if a == 2:
    if b < 18:
        result = "Before"
    if b > 18:
        result = "After"
    if b ==18:
        result = "Special"
if a > 2:
    result = "After"
print(result)

