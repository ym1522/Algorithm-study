import sys
from collections import Counter
a = list(map(int, sys.stdin.readline().split()))

count_items = Counter(a)
fre_item = count_items.most_common(n=1)

fre_value = fre_item[0][0]
fre_cnt = fre_item[0][1]

if fre_cnt == 3:
  print(fre_value * 1000 + 10000)
elif fre_cnt == 2:
  print(fre_value * 100 + 1000)
elif fre_cnt == 1:
  print(max(a) * 100)
  
  
# sorted 써서 set으로 중복제거 했으면 쉽게 했는데...
# lst = sorted(list(map(int, input().split())))

# if len(set(lst)) == 1:
#     print(10000 + lst[0]*1000)
# elif len(set(lst)) == 2:
#     print(1000 + lst[1]*100)
# else:
#     print(lst[2]*100)