# 암호해독기
# 메모리: 37524KB, 시간: 132ms

import sys
flag = 'y'
n = int(sys.stdin.readline())
cipher = list(map(int, sys.stdin.readline().split()))  # 암호문
plain = list(sys.stdin.readline().strip())  # 평문
dict = {0:" "}

for i in range(1, 27):
    dict[i] = chr(i+64)
    dict[i+26] = chr(i+26+70)

# 실패 --> 시간초과    
'''for i in cipher:
    if dict[i] in plain:
        plain.remove(dict[i])

if len(plain) == 0: print('y')
else: print('n')'''
    
    
plain.sort()
cipher.sort()
for i in range(n):
    if plain[i] != dict[cipher[i]]: flag = 'n'; break
print(flag)