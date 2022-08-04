# ascii로 접근
en_input = input()
cnt_list = [0 for x in range(26)]

for idx in en_input:
  cnt_list[ord(idx)-97] += 1
  
print(*cnt_list) # 배열이 아닌 값을 참조하기 위함