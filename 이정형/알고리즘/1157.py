word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
  # count 사용하여 개수 세기
  count = word.count(i)
  cnt.append(count)

# cnt 리스트 안에 max값이 2개 이상인 경우 물음표 반환
if cnt.count(max(cnt)) >= 2:
  print('?')
# 그게 아니라면 가장 많은 개수를 가지고 있는 문자를 대문자로 출력
else:
  print(word_list[(cnt.index(max(cnt)))].upper()) # index의 제일 첫번째만 반환하면 되므로