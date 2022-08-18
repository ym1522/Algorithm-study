a = input()
b = input()

for i in range(3):
  # 문자열 뒤에서 부터 곱해주면 됨, 이 식은 세자리 수 곲에 한정함
  print(int(a) * int(b[2-i]))

print(int(a) * int(b))