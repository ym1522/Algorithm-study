import sys

# 대기 시간 합의 최소값 구하기
N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

# 인출 시간 정렬
times.sort()

# 각 대기 시간은 이전 순서의 대기 시간 + 본인의 인출 시간
total_time = [times[0]]
for t in times[1:]:
    total_time += [total_time[-1] + t]
print(sum(total_time))