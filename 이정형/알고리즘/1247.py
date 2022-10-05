import sys
# 처음엔 input()으로 그냥 받았는데 시간 초과 발생
for i in range(3):
  temp_li = []
  for j in range(int(sys.stdin.readline())):
    temp_li.append(int(sys.stdin.readline()))
  
  if sum(temp_li) > 0:
    print('+')
  elif sum(temp_li) < 0:
    print('-')
  else:
    print('0')
    