import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
  num_list[int(sys.stdin.readline())] += 1 # 여기 inside array 안써주면 메모리 초과 나옴

for i in range(10001):
  if num_list[i] != 0:
    for j in range(num_list[i]):
      print(i)