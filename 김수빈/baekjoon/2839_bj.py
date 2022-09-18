def solution(N):
    cnt = [-1] * (N // 5 + (N % 5) // 3 + 1)
    for i in range(len(cnt)):
        new_n = N - (i * 5)
        if new_n < 0: continue
        cnt[i] = int(new_n / 3) + i if new_n % 3 == 0 else -1
    
    cnt = list(filter(lambda x: x > 0,cnt))
    if not cnt: return -1
    return min(cnt)

N = int(input())
print(solution(N))