# 4675 - 셀프 넘버
# 메모리: 31860KB, 시간: 944ms

not_self_num = []
self_num = []

for i in range(1, 10001):
    i = str(i)
    self_num.append(i)
    tmp = int(i)
    for j in range(len(i)):
        tmp += int(i[j])
    tmp = str(tmp)
    not_self_num.append(tmp)

for i in range(1, 10001):
    i = str(i)
    if i in not_self_num:
        self_num.remove(i)

print(*self_num, sep='\n')


# ------ 더 간단한 풀이 가능 ------
natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):       # i = 850       
    for j in str(i):            # j = "8", "5", "0"
        i += int(j)             # 850 + 8 + 5 + 0, i = 863
    generated_num.add(i)        # 생성자가 있는 숫자들

self_num = sorted(natural_num - generated_num)
print(*self_num, sep='\n')

'''
이렇게 하면 굳이 반복문 두 번 쓰지 않아도 됨 ㅜㅜ
'''