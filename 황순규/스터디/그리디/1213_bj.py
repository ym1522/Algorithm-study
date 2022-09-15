import sys

S = sys.stdin.readline().strip()
alphabet = [chr(ord('A')+i) for i in range(26)] # 알파벳 리스트 생성
cnt = {}
answer = ''
temp = ''

flag = True

for i in alphabet: 
    cnt[i] = S.count(i) # 문자열 내의 알파벳 개수 세기

for i in cnt:
    if cnt[i] % 2 == 0: # 알파벳 개수가 짝수이면 개수/2 만큼 더해주기
        answer += i * (cnt[i]//2) 
    else:
        answer += i * (cnt[i]//2)
        temp += i

if len(temp) >= 2:
    print("I'm Sorry Hansoo")
else:
    print(answer + temp + answer[::-1])
