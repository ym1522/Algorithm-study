#2월 18일 = special

a = int(input())
b = int(input())

if a ==2:
    if b == 18:
        print('Special')
    elif b < 18:
        print('Before')
    else:
        print('After')
elif a > 2:
    print('After')
else:
    print('Before')
