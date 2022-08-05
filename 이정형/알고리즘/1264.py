while True:
  s = input()
  result = 0
  if s == '#' and len(s) == 1:
    break
  else:
    lower_s = [] # 대문자를 소문자로 만들어서 한 번 만 연산
    collections = 'aeiou'
    for i in s:
      lower_s.append(i.lower())
    for j in collections:
      result += lower_s.count(j)
    print(result)
      